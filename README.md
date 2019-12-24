# Youtube_to_MP3_Converter

Written in Python.

## Introduction
    Takes youtube videos and converts them to mp3 files

## System Requirements
Name | Terminal Command
--- | ---
Homebrew | `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
Python 3 | `brew install python`
youtube_dl | `pip3 install youtube_dl` (download youtube video by URL)
libav | `brew install libav` (strips audio from youtube videos) (used by youtube_dl)                           
                                                
## Instructions
- open `songs.txt` and copy & paste URLs of youtube videos you'd like to convert to mp3 files
- open Terminal
- cd into `youtube-to-mp3` directory
- type `python3 downloader.py` in Terminal
- converted mp3 files are in `Songs` directory
