from __future__ import division, unicode_literals

import re
import json

from .fragment import FragmentFD


class YoutubeLiveChatReplayFD(FragmentFD):
    """ Downloads YouTube live chat replays fragment by fragment """

    FD_NAME = 'youtube_live_chat_replay'

    def real_download(self, filename, info_dict):
        video_id = info_dict['video_id']
        self.to_screen('[%s] Downloading live chat' % self.FD_NAME)

        test = self.params.get('test', False)

        ctx = {
            'filename': filename,
            'live': True,
            'total_frags': None,
        }

        def dl_fragment(url):
            headers = info_dict.get('http_headers', {})
            return self._download_fragment(ctx, url, info_dict, headers)

        def parse_yt_initial_data(data):
            window_patt = b'window\\["ytInitialData"\\]\\s*=\\s*(.*?)(?<=});'
            var_patt = b'var\\s+ytInitialData\\s*=\\s*(.*?)(?<=});'
            for patt in window_patt, var_patt:
                try:
                    raw_json = re.search(patt, data).group(1)
                    return json.loads(raw_json)
                except AttributeError:
                    continue
            return None

        def get_obj_value(obj, path):
            cur = obj
            try:
                for key in path:
                    cur = cur[key]
            except (KeyError, IndexError, TypeError):
                return None
            return cur

        def continuation_get_id(data):
            continuations = get_obj_value(data, ['continuations']) or []
            for continuation in continuations:
                if 'reloadContinuationData' in continuation:
                    return get_obj_value(continuation, ['reloadContinuationData', 'continuation'])
                if 'liveChatReplayContinuationData' in continuation:
                    return get_obj_value(continuation, ['liveChatReplayContinuationData', 'continuation'])
            return None

        self._prepare_and_start_frag_download(ctx)

        success, raw_fragment = dl_fragment(
            'https://www.youtube.com/watch?v={}'.format(video_id))
        if not success:
            self.report_error('Video page download unsuccessful.')
            return False
        data = parse_yt_initial_data(raw_fragment)
        if data is None:
            self.report_error('Unable to parse ytInitialData.')
            return False
        data = get_obj_value(data, ['contents', 'twoColumnWatchNextResults', 'conversationBar', 'liveChatRenderer'])
        if data is None:
            self.report_error('Cannot find liveChatRenderer from ytInitialData.')
            return False
        continuation_id = continuation_get_id(data)
        # no data yet but required to call _append_fragment
        self._append_fragment(ctx, b'')

        first = True
        offset = None
        while continuation_id is not None:
            data = None
            if first:
                url = 'https://www.youtube.com/live_chat_replay?continuation={}'.format(continuation_id)
                success, raw_fragment = dl_fragment(url)
                if not success:
                    self.report_error('Live chat continuation download unsuccessful.')
                    return False
                data = parse_yt_initial_data(raw_fragment)
            else:
                url = ('https://www.youtube.com/live_chat_replay/get_live_chat_replay'
                       + '?continuation={}'.format(continuation_id)
                       + '&playerOffsetMs={}'.format(offset - 5000)
                       + '&hidden=false'
                       + '&pbj=1')
                success, raw_fragment = dl_fragment(url)
                if not success:
                    self.report_error('Live chat continuation download unsuccessful.')
                    return False
                data = get_obj_value(json.loads(raw_fragment), ['response'])

            first = False
            continuation_id = None

            live_chat_continuation = get_obj_value(data, ['continuationContents', 'liveChatContinuation'])
            if live_chat_continuation is None:
                self.report_error('Cannot find liveChatContinuation.')
                return False
            offset = None
            processed_fragment = bytearray()
            if 'actions' in live_chat_continuation:
                for action in live_chat_continuation['actions']:
                    if 'replayChatItemAction' in action:
                        replay_chat_item_action = action['replayChatItemAction']
                        offset = int(replay_chat_item_action['videoOffsetTimeMsec'])
                    processed_fragment.extend(
                        json.dumps(action, ensure_ascii=False).encode('utf-8') + b'\n')
                continuation_id = continuation_get_id(live_chat_continuation)

            self._append_fragment(ctx, processed_fragment)

            if test or offset is None:
                break

        self._finish_frag_download(ctx)

        return True
