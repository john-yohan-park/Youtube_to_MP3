'''
Name    John Park
Github  john-yohan-park
Date    12/23/2019
'''
# import libraries
from __future__ import unicode_literals # turn every string into unicode
import youtube_dl                       # download youtube video by URL
import os                               # create & navigate directories
from   sys import argv				    # accept command line arguments

# set up download configurations
config = {
	'format'              : 'bestaudio/best',
	'outtmpl'             : '%(title)s.%(ext)s',
	'nocheckcertificate'  : True,
	'postprocessors'      : [{
		'key'             : 'FFmpegExtractAudio',
		'preferredcodec'  : 'mp3',
		'preferredquality': '192',
	}],
}

# manage & navigate file
if not os.path.exists('Songs'): # if 'Songs' directory does not exist,
    os.mkdir('Songs')           # create it
os.chdir('Songs')               # make 'Songs' current working directory

# download
if len(argv)>1:										# if URL is provided as cmd line arg
	with youtube_dl.YoutubeDL(config) as dl:		# set up configs
		dl.download([argv[1]]) 				        # download song from URL
else:												# if not, get URLs from songs.txt
	with youtube_dl.YoutubeDL(config) as dl:        # instantiate youtube_dl with preset configs
		with open('../songs.txt', 'r') as txt_file: # open and read text file (../ moves us up one directory) ('r' for reading)
			for song_url in txt_file:               # for every song URL in text file
				dl.download([song_url])             # download song from URL
