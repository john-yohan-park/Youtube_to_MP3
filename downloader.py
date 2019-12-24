'''
Name    John Park
Github  john-yohan-park
Date    12/23/2019
'''
# import libraries
from __future__ import unicode_literals  # turn every string into unicode
import youtube_dl                        # download youtube video by url
import os                                # create/navigate directories

# configs
download_options = {
	'format'            : 'bestaudio/best',
	'outtmpl'           : '%(title)s.%(ext)s',
	'nocheckcertificate': True,
	'postprocessors'    : [{
		'key'             : 'FFmpegExtractAudio',
		'preferredcodec'  : 'mp3',
		'preferredquality': '192',
	}],
}

# file management / navigation
if not os.path.exists('Songs'):  # if 'Songs' directory does not exist,
    os.mkdir('Songs')            # create it
os.chdir('Songs')                # make 'Songs' current working directory

# download songs
with youtube_dl.YoutubeDL(download_options) as dl:  # instantiate youtube_dl with preset configs
	with open('../songs.txt', 'r') as txt_file:     # open and read text file (../ moves us up one directory) ('r' for reading)
		for song_url in txt_file:                   # for every song URL in text file
			dl.download([song_url])                 # download song from URL
