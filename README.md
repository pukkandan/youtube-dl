This is a fork of [youtube-dl](https://github.com/ytdl-org/youtube-dl)

[![](https://img.shields.io/badge/Fork-2020.10.19.01-brightgreen?style=for-the-badge&logo=GitHub)](https://github.com/pukkandan/youtube-dl)
[![](https://img.shields.io/badge/youtube--dl-2020.09.20-blue?style=for-the-badge&logo=GitHub)](https://github.com/ytdl-org/youtube-dl)

youtube-dl - download videos from youtube.com or other video platforms

- [CHANGES FROM ORIGINAL](#changes)
    * [New Features](#new-features)
    * [Fixes](#fixes)
    * [Other Changes](#other-changes)
- [ABOUT THIS FORK](#about-this-fork)
- [INSTALLATION](#installation)
- [DESCRIPTION](#description)
- [OPTIONS](#options)
    * [Network Options](#network-options)
    * [Geo Restriction](#geo-restriction)
    * [Video Selection](#video-selection)
    * [Download Options](#download-options)
    * [Filesystem Options](#filesystem-options)
    * [Thumbnail images](#thumbnail-images)
    * [Internet Shortcut Options](#internet-shortcut-options)
    * [Verbosity / Simulation Options](#verbosity--simulation-options)
    * [Workarounds](#workarounds)
    * [Video Format Options](#video-format-options)
    * [Subtitle Options](#subtitle-options)
    * [Authentication Options](#authentication-options)
    * [Adobe Pass Options](#adobe-pass-options)
    * [Post-processing Options](#post-processing-options)
- [CONFIGURATION](#configuration)
    * [Authentication with .netrc file](#authentication-with-netrc-file)
- [OUTPUT TEMPLATE](#output-template)
    * [Output template and Windows batch files](#output-template-and-windows-batch-files)
- [FORMAT SELECTION](#format-selection)
- [MORE](#more)
- [COPYRIGHT](#copyright)


# CHANGES
See [Commits](https://github.com/pukkandan/youtube-dl/commits) for more details

### New Features

#### 2020.10.19.01
* **Negative Options:** `--no-download-archive`, `--resize-buffer`, `--part`, `--mtime`, `--no-keep-fragments`, `--no-cookies`, `--no-write-annotations`, `--no-write-info-json`, `--no-write-description`, `--no-write-thumbnail`, `--youtube-include-dash-manifest`, `--post-overwrites`, `--no-keep-video`, `--no-embed-subs`, `--no-embed-thumbnail`, `--no-add-metadata`

#### 2020.10.17.01
* **Live Chat:** `--write-sub --sub-lang live_chat` by @siikamiika

#### 2020.09.22.00
* **Format Sort:** `--format-sort`, `--format-sort-force`
* **Negative Options:** `--no-include-ads`, `--no-write-sub`, `--no-write-auto-sub`, `--no-playlist-reverse`, `--no-restrict-filenames`, `--youtube-include-dash-manifest`, `--no-format-sort-force`
* **Shortcut Options:** `--write-link`, `--write-url-link`, `--write-webloc-link`, `--write-desktop-link` by @h-h-h-h
* `--flat-videos`
* `--remux-video` by @Zocker1999NET
* `--break-on-existing` by @gergesh
* `--force-write-archive` by @h-h-h-h

### Fixes

#### 2020.10.19.00
* [Partially](https://github.com/pukkandan/youtube-dl/pull/18#issuecomment-711398332) fix youtube and feeds by @xarantolus
* Fix age-gated videos by @blackjack4494

#### 2020.10.17.02
* Fix for issue with external downloaders introduced by [#17](https://github.com/pukkandan/youtube-dl/pull/17)

#### 2020.09.23.00
* Dropped [#8](https://github.com/pukkandan/youtube-dl/pull/8). The issue this addresses has been fixed in the main repo

#### 2020.09.22.00
* Fix youtube chapters extractor by @gschizas
* Fix youtube description by @randombyte-developer
* Fix embedding thumbnails in mkv by @MrDoritos
* Fix embedding thumbnails in mp3 by @pauldubois98

### Other Changes

#### 2020.10.19.01
* **Format Sort:** Added `-S` as an alias for `--format-sort`
* **Negative Options:** Added aliases `--no-abort-on-error`, `--no-ignore-errors`, `--no-config`, `--no-abort-on-unavailable-fragment`, `--no-skip-unavailable-fragments`, `--no-youtube-include-dash-manifest`, `--no-youtube-skip-dash-manifest`, `--no-prefer-ffmpeg`, `--no-prefer-avconv`
* **Default:** Enabled `--ignore-errors` (Breaks backward compatibility)
* **Deprecated:** `--id` - Same as `--output %(id)s.%(ext)s`
* Minor changes to code (that doesn't change functionality)

#### 2020.10.17.00
* **Format Selection:** Any arbitrary field can be now used to filter formats in `-f`

#### 2020.10.16.01
* **Format Sort:** Changed default sort order. (Breaks backward compatibility)
* **Format Selection:** 'bestvideo' and 'worstvideo' may now download formats that also has audio (Breaks backward compatibility)

#### 2020.10.16.00
* **Format Sort:** Added some new fields and renamed old fields (Breaks backward compatibility)

#### 2020.09.22.00
* Restructured README.md

#### 2020.09.21.00
* Created this fork


# ABOUT THIS FORK

### Why does this fork exist?

[youtube-dl](https://github.com/ytdl-org/youtube-dl) currently have over 700 open pull requests and 3100 open issues. The project has very few maintainers and considering their very strict policies on merges, it makes sense that they are not able to look into and fix this massive amount of backlog. However,  there are some of these pull requests that I really want to use. So I created this fork and am pulling all the things I need into it. If anyone else wants to use this fork, feel free to do so. I personally use youtube-dl quite a lot, so expect the fork to be frequently updated.

### Can I request a pull/feature?

I am not accepting any feature requests. You probably better off making the request on the original repository or [youtube-dlc](https://github.com/blackjack4494/youtube-dlc).

If you already have the code, it's a different story. Make the pull request, and I will merge it as long as it doesn't break anything else.


# INSTALLATION

I don't plan on making any releases. If anyone wants to create and maintain releases for this fork, please contact me.

You can clone / [download](https://github.com/pukkandan/youtube-dl/archive/master.zip) this repository and run it with `python youtube_dl/__main__.py <args>`. Alternatively, you can install the fork using `pip install --upgrade https://github.com/pukkandan/youtube-dl/archive/master.zip` and run it with `python -m youtube_dl <args>`.

In order to update, simply repeat the process.


# DESCRIPTION

**youtube-dl** is a command-line program to download videos from YouTube.com and a few more sites. It requires the Python interpreter, version 2.6, 2.7, or 3.2+, and it is not platform specific. It should work on your Unix box, on Windows or on macOS. It is released to the public domain, which means you can modify it, redistribute it or use it however you like.

    youtube-dl [OPTIONS] [--] URL [URL...]

# OPTIONS
    -h, --help                       Print this help text and exit
    --version                        Print program version and exit
    -U, --update                     (Doesn't work since there is no release) 
                                     Update this program to latest version. Make
                                     sure that you have sufficient permissions
                                     (run with sudo if needed)
                                     
    -i, --ignore-errors              Continue on download errors, for example to
                                     skip unavailable videos in a playlist (default)
                                     (Same as --no-abort-on-error)
    --abort-on-error                 Abort downloading of further videos if an error
                                     occurs (Same as --no-ignore-errors)
    --dump-user-agent                Display the current browser identification
    --list-extractors                List all supported extractors
    --extractor-descriptions         Output descriptions of all supported
                                     extractors
    --force-generic-extractor        Force extraction to use the generic
                                     extractor
    --default-search PREFIX          Use this prefix for unqualified URLs. For
                                     example "gvsearch2:" downloads two videos
                                     from google videos for youtube-dl "large
                                     apple". Use the value "auto" to let
                                     youtube-dl guess ("auto_warning" to emit a
                                     warning when guessing). "error" just throws
                                     an error. The default value "fixup_error"
                                     repairs broken URLs, but emits an error if
                                     this is not possible instead of searching.
    --ignore-config, --no-config     Do not read configuration files. When given
                                     in the global configuration file
                                     /etc/youtube-dl.conf: Do not read the user
                                     configuration in ~/.config/youtube-
                                     dl/config (%APPDATA%/youtube-dl/config.txt
                                     on Windows)
    --config-location PATH           Location of the configuration file; either
                                     the path to the config or its containing
                                     directory.
    --flat-playlist                  Do not extract the videos of a playlist,
                                     only list them.
    --flat-videos                    Do not resolve the video urls.
    --mark-watched                   Mark videos watched (YouTube only)
    --no-mark-watched                Do not mark videos watched (YouTube only)
    --no-color                       Do not emit color codes in output

## Network Options:
    --proxy URL                      Use the specified HTTP/HTTPS/SOCKS proxy.
                                     To enable SOCKS proxy, specify a proper
                                     scheme. For example
                                     socks5://127.0.0.1:1080/. Pass in an empty
                                     string (--proxy "") for direct connection
    --socket-timeout SECONDS         Time to wait before giving up, in seconds
    --source-address IP              Client-side IP address to bind to
    -4, --force-ipv4                 Make all connections via IPv4
    -6, --force-ipv6                 Make all connections via IPv6

## Geo Restriction:
    --geo-verification-proxy URL     Use this proxy to verify the IP address for
                                     some geo-restricted sites. The default
                                     proxy specified by --proxy (or none, if the
                                     option is not present) is used for the
                                     actual downloading.
    --geo-bypass                     Bypass geographic restriction via faking
                                     X-Forwarded-For HTTP header
    --no-geo-bypass                  Do not bypass geographic restriction via
                                     faking X-Forwarded-For HTTP header
    --geo-bypass-country CODE        Force bypass geographic restriction with
                                     explicitly provided two-letter ISO 3166-2
                                     country code
    --geo-bypass-ip-block IP_BLOCK   Force bypass geographic restriction with
                                     explicitly provided IP block in CIDR
                                     notation

## Video Selection:
    --playlist-start NUMBER          Playlist video to start at (default is 1)
    --playlist-end NUMBER            Playlist video to end at (default is last)
    --playlist-items ITEM_SPEC       Playlist video items to download. Specify
                                     indices of the videos in the playlist
                                     separated by commas like: "--playlist-items
                                     1,2,5,8" if you want to download videos
                                     indexed 1, 2, 5, 8 in the playlist. You can
                                     specify range: "--playlist-items
                                     1-3,7,10-13", it will download the videos
                                     at index 1, 2, 3, 7, 10, 11, 12 and 13.
    --match-title REGEX              Download only matching titles (regex or
                                     caseless sub-string)
    --reject-title REGEX             Skip download for matching titles (regex or
                                     caseless sub-string)
    --max-downloads NUMBER           Abort after downloading NUMBER files
    --min-filesize SIZE              Do not download any videos smaller than
                                     SIZE (e.g. 50k or 44.6m)
    --max-filesize SIZE              Do not download any videos larger than SIZE
                                     (e.g. 50k or 44.6m)
    --date DATE                      Download only videos uploaded in this date.
                                     The date can be "YYYYMMDD" or in the format
                                     "(now|today)[+-][0-9](day|week|month|year)(s)?"
    --datebefore DATE                Download only videos uploaded on or before
                                     this date (i.e. inclusive). The date formats  
                                     accepted is the same as --date
    --dateafter DATE                 Download only videos uploaded on or after
                                     this date (i.e. inclusive). The date formats  
                                     accepted is the same as --date
    --min-views COUNT                Do not download any videos with less than
                                     COUNT views
    --max-views COUNT                Do not download any videos with more than
                                     COUNT views
    --match-filter FILTER            Generic video filter. Specify any key (see
                                     the "OUTPUT TEMPLATE" for a list of
                                     available keys) to match if the key is
                                     present, !key to check if the key is not
                                     present, key > NUMBER (like "comment_count
                                     > 12", also works with >=, <, <=, !=, =) to
                                     compare against a number, key = 'LITERAL'
                                     (like "uploader = 'Mike Smith'", also works
                                     with !=) to match against a string literal
                                     and & to require multiple matches. Values
                                     which are not known are excluded unless you
                                     put a question mark (?) after the operator.
                                     For example, to only match videos that have
                                     been liked more than 100 times and disliked
                                     less than 50 times (or the dislike
                                     functionality is not available at the given
                                     service), but who also have a description,
                                     use --match-filter "like_count > 100 &
                                     dislike_count <? 50 & description" .
    --no-playlist                    Download only the video, if the URL refers
                                     to a video and a playlist.
    --yes-playlist                   Download the playlist, if the URL refers to
                                     a video and a playlist.
    --age-limit YEARS                Download only videos suitable for the given
                                     age
    --download-archive FILE          Download only videos not listed in the
                                     archive file. Record the IDs of all
                                     downloaded videos in it.
    --no-download-archive            Do not use archive file (default)
    --break-on-existing              Stop the download process after attempting
                                     to download a file that's in the archive.
    --include-ads                    Download advertisements as well
                                     (experimental)
    --no-include-ads                 Do not download advertisements (default)

## Download Options:
    -r, --limit-rate RATE            Maximum download rate in bytes per second
                                     (e.g. 50K or 4.2M)
    -R, --retries RETRIES            Number of retries (default is 10), or
                                     "infinite".
    --fragment-retries RETRIES       Number of retries for a fragment (default
                                     is 10), or "infinite" (DASH, hlsnative and
                                     ISM)
    --skip-unavailable-fragments     Skip unavailable fragments for DASH,
                                     hlsnative and ISM (default)
                                     (Same as --no-abort-on-unavailable-fragment)
    --abort-on-unavailable-fragment  Abort downloading when some fragment is not
                                     available
                                     (Same as --no-skip-unavailable-fragments)
    --keep-fragments                 Keep downloaded fragments on disk after
                                     downloading is finished
    --no-keep-fragments              Delete downloaded fragments after downloading
                                     is finished (default)
    --buffer-size SIZE               Size of download buffer (e.g. 1024 or 16K)
                                     (default is 1024)
    --resize-buffer                  The buffer size is automatically resized from 
                                     an initial value of --buffer-size (default)
    --no-resize-buffer               Do not automatically adjust the buffer
                                     size
    --http-chunk-size SIZE           Size of a chunk for chunk-based HTTP
                                     downloading (e.g. 10485760 or 10M) (default
                                     is disabled). May be useful for bypassing
                                     bandwidth throttling imposed by a webserver
                                     (experimental)
    --playlist-reverse               Download playlist videos in reverse order
    --no-playlist-reverse            Download playlist videos in default order
    --playlist-random                Download playlist videos in random order
    --xattr-set-filesize             Set file xattribute ytdl.filesize with
                                     expected file size
    --hls-prefer-native              Use the native HLS downloader instead of
                                     ffmpeg
    --hls-prefer-ffmpeg              Use ffmpeg instead of the native HLS
                                     downloader
    --hls-use-mpegts                 Use the mpegts container for HLS videos,
                                     allowing to play the video while
                                     downloading (some players may not be able
                                     to play it)
    --external-downloader COMMAND    Use the specified external downloader.
                                     Currently supports
                                     aria2c,avconv,axel,curl,ffmpeg,httpie,wget
    --external-downloader-args ARGS  Give these arguments to the external
                                     downloader

## Filesystem Options:
    -a, --batch-file FILE            File containing URLs to download ('-' for
                                     stdin), one URL per line. Lines starting
                                     with '#', ';' or ']' are considered as
                                     comments and ignored.
    --id                             Use only video ID in file name
    -o, --output TEMPLATE            Output filename template, see the "OUTPUT
                                     TEMPLATE" for all the info
    --autonumber-start NUMBER        Specify the start value for %(autonumber)s
                                     (default is 1)
    --restrict-filenames             Restrict filenames to only ASCII
                                     characters, and avoid "&" and spaces in
                                     filenames
    --no-restrict-filenames          Allow Unicode characters, "&" and spaces
                                     in filenames (default)
    -w, --no-overwrites              Do not overwrite files
    -c, --continue                   Resume partially downloaded files (default)
    --no-continue                    Do not resume partially downloaded files
                                     (restart from beginning)
    --part                           Use .part files instead of writing directly 
                                     into output file (default)
    --no-part                        Do not use .part files - write directly
                                     into output file
    --mtime                          Use the Last-modified header to set the 
                                     file modification time
    --no-mtime                       Do not use the Last-modified header to set
                                     the file modification time
    --write-description              Write video description to a .description
                                     file
    --no-write-description           Do not write video description (default)
    --write-info-json                Write video metadata to a .info.json file
    --no-write-info-json             Do not write video metadata (default)
    --write-annotations              Write video annotations to a
                                     .annotations.xml file
    --no-write-annotations           Do not write video annotations (default)
    --load-info-json FILE            JSON file containing the video information
                                     (created with the "--write-info-json"
                                     option)
    --cookies FILE                   File to read cookies from and dump cookie
                                     jar in
    --no-cookies                     Do not read/dump cookies (default)
    --cache-dir DIR                  Location in the filesystem where youtube-dl
                                     can store some downloaded information
                                     permanently. By default
                                     $XDG_CACHE_HOME/youtube-dl or
                                     ~/.cache/youtube-dl . At the moment, only
                                     YouTube player files (for videos with
                                     obfuscated signatures) are cached, but that
                                     may change.
    --no-cache-dir                   Disable filesystem caching
    --rm-cache-dir                   Delete all filesystem cache files

## Thumbnail images:
    --write-thumbnail                Write thumbnail image to disk
    --no-write-thumbnail             Do not write thumbnail image to disk
    --write-all-thumbnails           Write all thumbnail image formats to disk
    --list-thumbnails                Simulate and list all available thumbnail
                                     formats


## Internet Shortcut Options:
    --write-link                     Write an internet shortcut file, depending on 
                                     the current platform (.url/.webloc/.desktop). 
                                     The URL may be cached by the OS.
    --write-url-link                 Write a Windows internet shortcut file (.url). 
                                     Note that the OS caches the URL based on the file path.
    --write-webloc-link              Write a macOS internet shortcut file (.webloc)
    --write-desktop-link             Write a Linux internet shortcut file (.desktop)

## Verbosity / Simulation Options:
    -q, --quiet                      Activate quiet mode
    --no-warnings                    Ignore warnings
    -s, --simulate                   Do not download the video and do not write
                                     anything to disk
    --skip-download                  Do not download the video
    -g, --get-url                    Simulate, quiet but print URL
    -e, --get-title                  Simulate, quiet but print title
    --get-id                         Simulate, quiet but print id
    --get-thumbnail                  Simulate, quiet but print thumbnail URL
    --get-description                Simulate, quiet but print video description
    --get-duration                   Simulate, quiet but print video length
    --get-filename                   Simulate, quiet but print output filename
    --get-format                     Simulate, quiet but print output format
    -j, --dump-json                  Simulate, quiet but print JSON information.
                                     See the "OUTPUT TEMPLATE" for a description
                                     of available keys.
    -J, --dump-single-json           Simulate, quiet but print JSON information
                                     for each command-line argument. If the URL
                                     refers to a playlist, dump the whole
                                     playlist information in a single line.
    --print-json                     Be quiet and print the video information as
                                     JSON (video is still being downloaded).
    --force-write-archive'           Force download archive entries to be written 
                                     as far as no errors occur, even if
                                     --skip-download or any simulation switch is used.
    --newline                        Output progress bar as new lines
    --no-progress                    Do not print progress bar
    --console-title                  Display progress in console titlebar
    -v, --verbose                    Print various debugging information
    --dump-pages                     Print downloaded pages encoded using base64
                                     to debug problems (very verbose)
    --write-pages                    Write downloaded intermediary pages to
                                     files in the current directory to debug
                                     problems
    --print-traffic                  Display sent and read HTTP traffic
    -C, --call-home                  Contact the youtube-dl server for debugging
    --no-call-home                   Do NOT contact the youtube-dl server for
                                     debugging

## Workarounds:
    --encoding ENCODING              Force the specified encoding (experimental)
    --no-check-certificate           Suppress HTTPS certificate validation
    --prefer-insecure                Use an unencrypted connection to retrieve
                                     information about the video. (Currently
                                     supported only for YouTube)
    --user-agent UA                  Specify a custom user agent
    --referer URL                    Specify a custom referer, use if the video
                                     access is restricted to one domain
    --add-header FIELD:VALUE         Specify a custom HTTP header and its value,
                                     separated by a colon ':'. You can use this
                                     option multiple times
    --bidi-workaround                Work around terminals that lack
                                     bidirectional text support. Requires bidiv
                                     or fribidi executable in PATH
    --sleep-interval SECONDS         Number of seconds to sleep before each
                                     download when used alone or a lower bound
                                     of a range for randomized sleep before each
                                     download (minimum possible number of
                                     seconds to sleep) when used along with
                                     --max-sleep-interval.
    --max-sleep-interval SECONDS     Upper bound of a range for randomized sleep
                                     before each download (maximum possible
                                     number of seconds to sleep). Must only be
                                     used along with --min-sleep-interval.

## Video Format Options:
    -f, --format FORMAT              Video format code, see the "FORMAT
                                     SELECTION" for all the info
                                     Note that the OS caches the URL based on the file path.
    -S, --format-sort SORTORDER      Sort the formats by the fields given. 
                                     Default order: avoid_bad, has_video, extractor, language, 
                                     height, width, proto, fps, codec, filesize, filesize_approx, 
                                     tbr, vbr, has_audio, abr, audio_codec, quality, source, format_id.
                                     Prefix the field (except format_id) by a + to 
                                     perform the sort in reverse. Suffix the field with 
                                     :NUMBER to give highest preference to "NUMBER". 
                                     Examples: 1) 
                                     "-f bestvideo --format-sort +height:720,fps,+filesize" 
                                     gets the video with the smallest filesize with the 
                                     largest fps with the smallest height>=720 (or 
                                     largest height available if there is no such format). 
                                     2) "-f bestvideo --format-sort height:720,tbr" gets the 
                                     video with largest bitrate with the largest height<=720 
                                     (or smallest height available if there is no such format)
    --format-sort-force              User specified sort order takes priority even over
                                     avoid_bad, has_video, extractor and language. 
                                     These fields normally filter out the undesirable formats. 
                                     So use this option with caution. 
    --no-format-sort-force           avoid_bad, has_video, extractor and language
                                     takes priority over any user specified sort order (default)
    --all-formats                    Download all available video formats
    --prefer-free-formats            Prefer free video formats unless a specific
                                     one is requested
    -F, --list-formats               List all available formats of requested
                                     videos
    --youtube-skip-dash-manifest     Do not download the DASH manifests and
                                     related data on YouTube videos
                                     (Same as --no-youtube-include-dash-manifest)
    --youtube-include-dash-manifest  Download the DASH manifests and related data 
                                     on YouTube videos (default)
                                     (Same as --no-youtube-skip-dash-manifest)
    --merge-output-format FORMAT     If a merge is required (e.g.
                                     bestvideo+bestaudio), output to given
                                     container format. One of mkv, mp4, ogg,
                                     webm, flv. Ignored if no merge is required

## Subtitle Options:
    --write-sub                      Write subtitle file
    --write-sub                      Do not write subtitle file (default)
    --write-auto-sub                 Write automatically generated subtitle file
                                     (YouTube only)
    --write-sub                      Do not write automatically generated
                                     subtitle file (default)
    --all-subs                       Download all the available subtitles of the
                                     video
    --list-subs                      List all available subtitles for the video
    --sub-format FORMAT              Subtitle format, accepts formats
                                     preference, for example: "srt" or
                                     "ass/srt/best"
    --sub-lang LANGS                 Languages of the subtitles to download
                                     (optional) separated by commas, use --list-
                                     subs for available language tags

## Authentication Options:
    -u, --username USERNAME          Login with this account ID
    -p, --password PASSWORD          Account password. If this option is left
                                     out, youtube-dl will ask interactively.
    -2, --twofactor TWOFACTOR        Two-factor authentication code
    -n, --netrc                      Use .netrc authentication data
    --video-password PASSWORD        Video password (vimeo, smotri, youku)

## Adobe Pass Options:
    --ap-mso MSO                     Adobe Pass multiple-system operator (TV
                                     provider) identifier, use --ap-list-mso for
                                     a list of available MSOs
    --ap-username USERNAME           Multiple-system operator account login
    --ap-password PASSWORD           Multiple-system operator account password.
                                     If this option is left out, youtube-dl will
                                     ask interactively.
    --ap-list-mso                    List all supported multiple-system
                                     operators

## Post-processing Options:
    -x, --extract-audio              Convert video files to audio-only files
                                     (requires ffmpeg or avconv and ffprobe or
                                     avprobe)
    --audio-format FORMAT            Specify audio format: "best", "aac",
                                     "flac", "mp3", "m4a", "opus", "vorbis", or
                                     "wav"; "best" by default; No effect without
                                     -x
    --audio-quality QUALITY          Specify ffmpeg/avconv audio quality, insert
                                     a value between 0 (better) and 9 (worse)
                                     for VBR or a specific bitrate like 128K
                                     (default 5)
    --remux-video FORMAT             Remux the video to another container format
                                     if necessary (currently supported: mp4|mkv,
                                     target container format must support video
                                     / audio encoding, remuxing may fail)
    --recode-video FORMAT            Encode the video to another format if
                                     necessary (currently supported:
                                     mp4|flv|ogg|webm|mkv|avi)
    --postprocessor-args ARGS        Give these arguments to the postprocessor
    -k, --keep-video                 Keep the intermediate video file on disk 
                                     after post-processing
    --no-keep-video                  Delete the intermediate video file after 
                                     post-processing (default)
    --post-overwrites                Overwrite post-processed files (default)
    --no-post-overwrites             Do not overwrite post-processed files
    --embed-subs                     Embed subtitles in the video (only for mp4,
                                     webm and mkv videos)
    --no-embed-subs                  Do not embed subtitles in the video (default)
    --embed-thumbnail                Embed thumbnail in the audio as cover art
    --no-embed-thumbnail             Do not embed thumbnail (default)
    --add-metadata                   Write metadata to the video file
    --no-add-metadata                Do not write metadata (default)
    --metadata-from-title FORMAT     Parse additional metadata like song title /
                                     artist from the video title. The format
                                     syntax is the same as --output. Regular
                                     expression with named capture groups may
                                     also be used. The parsed parameters replace
                                     existing values. Example: --metadata-from-
                                     title "%(artist)s - %(title)s" matches a
                                     title like "Coldplay - Paradise". Example
                                     (regex): --metadata-from-title
                                     "(?P<artist>.+?) - (?P<title>.+)"
    --xattrs                         Write metadata to the video file's xattrs
                                     (using dublin core and xdg standards)
    --fixup POLICY                   Automatically correct known faults of the
                                     file. One of never (do nothing), warn (only
                                     emit a warning), detect_or_warn (the
                                     default; fix file if we can, warn
                                     otherwise)
    --prefer-avconv                  Prefer avconv over ffmpeg for running the
                                     postprocessors (Same as --no-prefer-ffmpeg)
    --prefer-ffmpeg                  Prefer ffmpeg over avconv for running the
                                     postprocessors (default)
                                     (Same as --no-prefer-avconv)
    --ffmpeg-location PATH           Location of the ffmpeg/avconv binary;
                                     either the path to the binary or its
                                     containing directory.
    --exec CMD                       Execute a command on the file after
                                     downloading and post-processing, similar to
                                     find's -exec syntax. Example: --exec 'adb
                                     push {} /sdcard/Music/ && rm {}'
    --convert-subs FORMAT            Convert the subtitles to other format
                                     (currently supported: srt|ass|vtt|lrc)

# CONFIGURATION

You can configure youtube-dl by placing any supported command line option to a configuration file. On Linux and macOS, the system wide configuration file is located at `/etc/youtube-dl.conf` and the user wide configuration file at `~/.config/youtube-dl/config`. On Windows, the user wide configuration file locations are `%APPDATA%\youtube-dl\config.txt` or `C:\Users\<user name>\youtube-dl.conf`. Note that by default configuration file may not exist so you may need to create it yourself.

For example, with the following configuration file youtube-dl will always extract the audio, not copy the mtime, use a proxy and save all videos under `Movies` directory in your home directory:
```
# Lines starting with # are comments

# Always extract audio
-x

# Do not copy the mtime
--no-mtime

# Use this proxy
--proxy 127.0.0.1:3128

# Save all videos under Movies directory in your home directory
-o ~/Movies/%(title)s.%(ext)s
```

Note that options in configuration file are just the same options aka switches used in regular command line calls thus there **must be no whitespace** after `-` or `--`, e.g. `-o` or `--proxy` but not `- o` or `-- proxy`.

You can use `--ignore-config` if you want to disable the configuration file for a particular youtube-dl run.

You can also use `--config-location` if you want to use custom configuration file for a particular youtube-dl run.

### Authentication with `.netrc` file

You may also want to configure automatic credentials storage for extractors that support authentication (by providing login and password with `--username` and `--password`) in order not to pass credentials as command line arguments on every youtube-dl execution and prevent tracking plain text passwords in the shell command history. You can achieve this using a [`.netrc` file](https://stackoverflow.com/tags/.netrc/info) on a per extractor basis. For that you will need to create a `.netrc` file in your `$HOME` and restrict permissions to read/write by only you:
```
touch $HOME/.netrc
chmod a-rwx,u+rw $HOME/.netrc
```
After that you can add credentials for an extractor in the following format, where *extractor* is the name of the extractor in lowercase:
```
machine <extractor> login <login> password <password>
```
For example:
```
machine youtube login myaccount@gmail.com password my_youtube_password
machine twitch login my_twitch_account_name password my_twitch_password
```
To activate authentication with the `.netrc` file you should pass `--netrc` to youtube-dl or place it in the [configuration file](#configuration).

On Windows you may also need to setup the `%HOME%` environment variable manually. For example:
```
set HOME=%USERPROFILE%
```

# OUTPUT TEMPLATE

The `-o` option allows users to indicate a template for the output file names.

**tl;dr:** [navigate me to examples](#output-template-examples).

The basic usage is not to set any template arguments when downloading a single file, like in `youtube-dl -o funny_video.flv "https://some/video"`. However, it may contain special sequences that will be replaced when downloading each video. The special sequences may be formatted according to [python string formatting operations](https://docs.python.org/2/library/stdtypes.html#string-formatting). For example, `%(NAME)s` or `%(NAME)05d`. To clarify, that is a percent symbol followed by a name in parentheses, followed by formatting operations. Allowed names along with sequence type are:

 - `id` (string): Video identifier
 - `title` (string): Video title
 - `url` (string): Video URL
 - `ext` (string): Video filename extension
 - `alt_title` (string): A secondary title of the video
 - `display_id` (string): An alternative identifier for the video
 - `uploader` (string): Full name of the video uploader
 - `license` (string): License name the video is licensed under
 - `creator` (string): The creator of the video
 - `release_date` (string): The date (YYYYMMDD) when the video was released
 - `timestamp` (numeric): UNIX timestamp of the moment the video became available
 - `upload_date` (string): Video upload date (YYYYMMDD)
 - `uploader_id` (string): Nickname or id of the video uploader
 - `channel` (string): Full name of the channel the video is uploaded on
 - `channel_id` (string): Id of the channel
 - `location` (string): Physical location where the video was filmed
 - `duration` (numeric): Length of the video in seconds
 - `view_count` (numeric): How many users have watched the video on the platform
 - `like_count` (numeric): Number of positive ratings of the video
 - `dislike_count` (numeric): Number of negative ratings of the video
 - `repost_count` (numeric): Number of reposts of the video
 - `average_rating` (numeric): Average rating give by users, the scale used depends on the webpage
 - `comment_count` (numeric): Number of comments on the video
 - `age_limit` (numeric): Age restriction for the video (years)
 - `is_live` (boolean): Whether this video is a live stream or a fixed-length video
 - `start_time` (numeric): Time in seconds where the reproduction should start, as specified in the URL
 - `end_time` (numeric): Time in seconds where the reproduction should end, as specified in the URL
 - `format` (string): A human-readable description of the format 
 - `format_id` (string): Format code specified by `--format`
 - `format_note` (string): Additional info about the format
 - `width` (numeric): Width of the video
 - `height` (numeric): Height of the video
 - `resolution` (string): Textual description of width and height
 - `tbr` (numeric): Average bitrate of audio and video in KBit/s
 - `abr` (numeric): Average audio bitrate in KBit/s
 - `acodec` (string): Name of the audio codec in use
 - `asr` (numeric): Audio sampling rate in Hertz
 - `vbr` (numeric): Average video bitrate in KBit/s
 - `fps` (numeric): Frame rate
 - `vcodec` (string): Name of the video codec in use
 - `container` (string): Name of the container format
 - `filesize` (numeric): The number of bytes, if known in advance
 - `filesize_approx` (numeric): An estimate for the number of bytes
 - `protocol` (string): The protocol that will be used for the actual download
 - `extractor` (string): Name of the extractor
 - `extractor_key` (string): Key name of the extractor
 - `epoch` (numeric): Unix epoch when creating the file
 - `autonumber` (numeric): Five-digit number that will be increased with each download, starting at zero
 - `playlist` (string): Name or id of the playlist that contains the video
 - `playlist_index` (numeric): Index of the video in the playlist padded with leading zeros according to the total length of the playlist
 - `playlist_id` (string): Playlist identifier
 - `playlist_title` (string): Playlist title
 - `playlist_uploader` (string): Full name of the playlist uploader
 - `playlist_uploader_id` (string): Nickname or id of the playlist uploader

Available for the video that belongs to some logical chapter or section:

 - `chapter` (string): Name or title of the chapter the video belongs to
 - `chapter_number` (numeric): Number of the chapter the video belongs to
 - `chapter_id` (string): Id of the chapter the video belongs to

Available for the video that is an episode of some series or programme:

 - `series` (string): Title of the series or programme the video episode belongs to
 - `season` (string): Title of the season the video episode belongs to
 - `season_number` (numeric): Number of the season the video episode belongs to
 - `season_id` (string): Id of the season the video episode belongs to
 - `episode` (string): Title of the video episode
 - `episode_number` (numeric): Number of the video episode within a season
 - `episode_id` (string): Id of the video episode

Available for the media that is a track or a part of a music album:

 - `track` (string): Title of the track
 - `track_number` (numeric): Number of the track within an album or a disc
 - `track_id` (string): Id of the track
 - `artist` (string): Artist(s) of the track
 - `genre` (string): Genre(s) of the track
 - `album` (string): Title of the album the track belongs to
 - `album_type` (string): Type of the album
 - `album_artist` (string): List of all artists appeared on the album
 - `disc_number` (numeric): Number of the disc or other physical medium the track belongs to
 - `release_year` (numeric): Year (YYYY) when the album was released

Each aforementioned sequence when referenced in an output template will be replaced by the actual value corresponding to the sequence name. Note that some of the sequences are not guaranteed to be present since they depend on the metadata obtained by a particular extractor. Such sequences will be replaced with `NA`.

For example for `-o %(title)s-%(id)s.%(ext)s` and an mp4 video with title `youtube-dl test video` and id `BaW_jenozKcj`, this will result in a `youtube-dl test video-BaW_jenozKcj.mp4` file created in the current directory.

For numeric sequences you can use numeric related formatting, for example, `%(view_count)05d` will result in a string with view count padded with zeros up to 5 characters, like in `00042`.

Output templates can also contain arbitrary hierarchical path, e.g. `-o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s'` which will result in downloading each video in a directory corresponding to this path template. Any missing directory will be automatically created for you.

To use percent literals in an output template use `%%`. To output to stdout use `-o -`.

The current default template is `%(title)s-%(id)s.%(ext)s`.

In some cases, you don't want special characters such as 中, spaces, or &, such as when transferring the downloaded filename to a Windows system or the filename through an 8bit-unsafe channel. In these cases, add the `--restrict-filenames` flag to get a shorter title:

#### Output template and Windows batch files

If you are using an output template inside a Windows batch file then you must escape plain percent characters (`%`) by doubling, so that `-o "%(title)s-%(id)s.%(ext)s"` should become `-o "%%(title)s-%%(id)s.%%(ext)s"`. However you should not touch `%`'s that are not plain characters, e.g. environment variables for expansion should stay intact: `-o "C:\%HOMEPATH%\Desktop\%%(title)s.%%(ext)s"`.

#### Output template examples

Note that on Windows you may need to use double quotes instead of single.

```bash
$ youtube-dl --get-filename -o '%(title)s.%(ext)s' BaW_jenozKc
youtube-dl test video ''_ä↭𝕐.mp4    # All kinds of weird characters

$ youtube-dl --get-filename -o '%(title)s.%(ext)s' BaW_jenozKc --restrict-filenames
youtube-dl_test_video_.mp4          # A simple file name

# Download YouTube playlist videos in separate directory indexed by video order in a playlist
$ youtube-dl -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re

# Download all playlists of YouTube channel/user keeping each playlist in separate directory:
$ youtube-dl -o '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/user/TheLinuxFoundation/playlists

# Download Udemy course keeping each chapter in separate directory under MyVideos directory in your home
$ youtube-dl -u user -p password -o '~/MyVideos/%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s' https://www.udemy.com/java-tutorial/

# Download entire series season keeping each series and each season in separate directory under C:/MyVideos
$ youtube-dl -o "C:/MyVideos/%(series)s/%(season_number)s - %(season)s/%(episode_number)s - %(episode)s.%(ext)s" https://videomore.ru/kino_v_detalayah/5_sezon/367617

# Stream the video being downloaded to stdout
$ youtube-dl -o - BaW_jenozKc
```

# FORMAT SELECTION

**Note**: Also see `--format-sort`. It significantly simplifies complex format selections.
> **TODO**: Rewrite with examples using --format-sort

By default youtube-dl tries to download the best available quality, i.e. if you want the best quality you **don't need** to pass any special options, youtube-dl will guess it for you by **default**.

But sometimes you may want to download in a different format, for example when you are on a slow or intermittent connection. The key mechanism for achieving this is so-called *format selection* based on which you can explicitly specify desired format, select formats based on some criterion or criteria, setup precedence and much more.

The general syntax for format selection is `--format FORMAT` or shorter `-f FORMAT` where `FORMAT` is a *selector expression*, i.e. an expression that describes format or formats you would like to download.

**tl;dr:** [navigate me to examples](#format-selection-examples).

The simplest case is requesting a specific format, for example with `-f 22` you can download the format with format code equal to 22. You can get the list of available format codes for particular video using `--list-formats` or `-F`. Note that these format codes are extractor specific. 

You can also use a file extension (currently `3gp`, `aac`, `flv`, `m4a`, `mp3`, `mp4`, `ogg`, `wav`, `webm` are supported) to download the best quality format of a particular file extension served as a single file, e.g. `-f webm` will download the best quality format with the `webm` extension served as a single file.

You can also use special names to select particular edge case formats:

 - `best`: Select the best quality format represented by a single file with video and audio.
 - `worst`: Select the worst quality format represented by a single file with video and audio.
 - `bestvideo`: Select the best quality video-only format (e.g. DASH video). May not be available.
 - `worstvideo`: Select the worst quality video-only format. May not be available.
 - `bestaudio`: Select the best quality audio only-format. May not be available.
 - `worstaudio`: Select the worst quality audio only-format. May not be available.

For example, to download the worst quality video-only format you can use `-f worstvideo`.

If you want to download multiple videos and they don't have the same formats available, you can specify the order of preference using slashes. Note that slash is left-associative, i.e. formats on the left hand side are preferred, for example `-f 22/17/18` will download format 22 if it's available, otherwise it will download format 17 if it's available, otherwise it will download format 18 if it's available, otherwise it will complain that no suitable formats are available for download.

If you want to download several formats of the same video use a comma as a separator, e.g. `-f 22,17,18` will download all these three formats, of course if they are available. Or a more sophisticated example combined with the precedence feature: `-f 136/137/mp4/bestvideo,140/m4a/bestaudio`.

You can also filter the video formats by putting a condition in brackets, as in `-f "best[height=720]"` (or `-f "[filesize>10M]"`).

The following numeric meta fields can be used with comparisons `<`, `<=`, `>`, `>=`, `=` (equals), `!=` (not equals):

 - `filesize`: The number of bytes, if known in advance
 - `width`: Width of the video, if known
 - `height`: Height of the video, if known
 - `tbr`: Average bitrate of audio and video in KBit/s
 - `abr`: Average audio bitrate in KBit/s
 - `vbr`: Average video bitrate in KBit/s
 - `asr`: Audio sampling rate in Hertz
 - `fps`: Frame rate

Also filtering work for comparisons `=` (equals), `^=` (starts with), `$=` (ends with), `*=` (contains) and following string meta fields:

 - `ext`: File extension
 - `acodec`: Name of the audio codec in use
 - `vcodec`: Name of the video codec in use
 - `container`: Name of the container format
 - `protocol`: The protocol that will be used for the actual download, lower-case (`http`, `https`, `rtsp`, `rtmp`, `rtmpe`, `mms`, `f4m`, `ism`, `http_dash_segments`, `m3u8`, or `m3u8_native`)
 - `format_id`: A short description of the format

Any string comparison may be prefixed with negation `!` in order to produce an opposite comparison, e.g. `!*=` (does not contain).

Note that none of the aforementioned meta fields are guaranteed to be present since this solely depends on the metadata obtained by particular extractor, i.e. the metadata offered by the video hoster.

Formats for which the value is not known are excluded unless you put a question mark (`?`) after the operator. You can combine format filters, so `-f "[height <=? 720][tbr>500]"` selects up to 720p videos (or videos where the height is not known) with a bitrate of at least 500 KBit/s.

You can merge the video and audio of two formats into a single file using `-f <video-format>+<audio-format>` (requires ffmpeg or avconv installed), for example `-f bestvideo+bestaudio` will download the best video-only format, the best audio-only format and mux them together with ffmpeg/avconv.

Format selectors can also be grouped using parentheses, for example if you want to download the best mp4 and webm formats with a height lower than 480 you can use `-f '(mp4,webm)[height<480]'`.

Since the end of April 2015 and version 2015.04.26, youtube-dl uses `-f bestvideo+bestaudio/best` as the default format selection (see [#5447](https://github.com/ytdl-org/youtube-dl/issues/5447), [#5456](https://github.com/ytdl-org/youtube-dl/issues/5456)). If ffmpeg or avconv are installed this results in downloading `bestvideo` and `bestaudio` separately and muxing them together into a single file giving the best overall quality available. Otherwise it falls back to `best` and results in downloading the best available quality served as a single file. `best` is also needed for videos that don't come from YouTube because they don't provide the audio and video in two different files. If you want to only download some DASH formats (for example if you are not interested in getting videos with a resolution higher than 1080p), you can add `-f bestvideo[height<=?1080]+bestaudio/best` to your configuration file. Note that if you use youtube-dl to stream to `stdout` (and most likely to pipe it to your media player then), i.e. you explicitly specify output template as `-o -`, youtube-dl still uses `-f best` format selection in order to start content delivery immediately to your player and not to wait until `bestvideo` and `bestaudio` are downloaded and muxed.

If you want to preserve the old format selection behavior (prior to youtube-dl 2015.04.26), i.e. you want to download the best available quality media served as a single file, you should explicitly specify your choice with `-f best`. You may want to add it to the [configuration file](#configuration) in order not to type it every time you run youtube-dl.

#### Format selection examples

Note that on Windows you may need to use double quotes instead of single.

```bash
# Download best mp4 format available or any other best if no mp4 available
$ youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'

# Download best format available but no better than 480p
$ youtube-dl -f 'bestvideo[height<=480]+bestaudio/best[height<=480]'

# Download best video only format but no bigger than 50 MB
$ youtube-dl -f 'best[filesize<50M]'

# Download best format available via direct link over HTTP/HTTPS protocol
$ youtube-dl -f '(bestvideo+bestaudio/best)[protocol^=http]'

# Download the best video format and the best audio format without merging them
$ youtube-dl -f 'bestvideo,bestaudio' -o '%(title)s.f%(format_id)s.%(ext)s'
```
Note that in the last example, an output template is recommended as bestvideo and bestaudio may have the same file name.

# MORE
For FAQ, Developer Instructions etc., see the [original README](https://github.com/ytdl-org/youtube-dl)

# COPYRIGHT

youtube-dl is released into the public domain by the copyright holders.

This README file was originally written by [Daniel Bolton](https://github.com/dbbolton) and is likewise released into the public domain.
