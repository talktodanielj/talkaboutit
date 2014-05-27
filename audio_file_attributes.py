#!/usr/bin/env python
# coding: utf-8

import os
import mutagen
import shutil
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError

#filename = "/home/danielj/Documents/python/01 - Baby Will You Please Help Me.mp3"

#fp = open(filename, "rb")

#if fp.closed != True:
#    print(fp.name)
#    print(
#    fp.close()


#audio = EasyID3("/home/danielj/Documents/Music/06 - Don't Be Denied.mp3")
#print audio.info.length, audio.info.bitrate
#print(audio.pprint())
#print("Artist:" + str(audio["artist"]).replace("[u'", "").replace("']", ""))
#print("Album:" + str(audio["album"]).replace("[u\"", "").replace("\"]", "").replace("[u'", "").replace("']", ""))
#print("Track number:" + str(audio["tracknumber"]).replace("[u'", "").replace("']", ""))
##print("Track Title:" + str(audio["title"]).replace("[u'", "").replace("']", ""))

sourceDirectory = "/home/danielj/Music"

for file in os.listdir(sourceDirectory):
    if file.endswith(".mp3"):
        print file
        filepath = os.path.join(sourceDirectory, file);
        try:
	    audio = EasyID3(filepath)
            #print(audio.pprint())
        
            artist = str(audio["artist"]).replace("[u'", "").replace("']", "")
        
            if artist == "":
	      artist = "Unknown artist"
        
            artistFolder = os.path.join(sourceDirectory, artist)
            if not os.path.exists(artistFolder):
	        os.makedirs(artistFolder)
	
	    album = str(audio["album"]).replace("[u\"", "").replace("\"]", "").replace("[u'", "").replace("']", "")
	
	    if album == "":
	      album = "Unknown album"
	
	    albumFolder = os.path.join(artistFolder, album)
	    if not os.path.exists(albumFolder):
	        os.makedirs(albumFolder)
	
	    shutil.move(filepath, albumFolder)
	    
        except ID3NoHeaderError:
	    print "File not processes"
	except KeyError:
	    print "Key error"
	    
        #if not os.path.exists(directory):
    #os.makedirs(directory)
        
        