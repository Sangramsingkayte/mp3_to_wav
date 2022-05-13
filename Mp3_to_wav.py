#!/usr/bin/env python
# Sangramsing Kayte


import os
from pydub import AudioSegment

path = "/Users/sing/Speech/Mp3_to_wav/mp3" # Your mp3 folder path and all data save as a same folder

#Change working directory
os.chdir (path)

audio_files = os.listdir()

# You dont need the number of files in the folder, just iterate over them directly using:
for file in audio_files:
    #spliting the file into the name and the extension
    name, ext = os.path.splitext(file)
    if ext == ".mp3":
       mp3_sound = AudioSegment.from_mp3(file)
       #rename them using the old name + ".wav"
       mp3_sound.export("{0}.wav".format(name), format="wav")