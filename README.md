# Youtube_to_MP3_Converter

Written in Python

## Introduction
Convert youtube videos to mp3 files

## System Requirements
Name       | Terminal Command
---        | ---
Homebrew   | `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
Python 3   | `brew install python`
youtube_dl | `pip3 install youtube_dl` (download youtube video by URL)
libav      | `brew install libav` (strips audio from youtube videos)

## Instructions
***Option 1:*** Download 1 song by passing its URL as command line argument
- open Terminal
- cd into `youtube-to-mp3` directory
- type `python3 downloader.py "URL"` in Terminal
    - substitute `URL` with desired youtube video's `URL`
    - wrap the `URL` in double or single quotes (as depicted above)
- converted mp3 file is in `Songs` directory

***Option 2:*** Download multiple songs from list of URLs in `songs.txt`
- open `songs.txt`
- copy & paste URLs (1 per line)
- open Terminal
- cd into `youtube-to-mp3` directory
- type `python3 downloader.py` in Terminal
- converted mp3 files are in `Songs` directory
