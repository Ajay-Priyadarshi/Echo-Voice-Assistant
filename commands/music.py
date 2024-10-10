# commands/music.py

import os
from commands.utils import say
from data.music import MUSIC 

def playMusic(song):
    songPath = MUSIC.get(song.lower())
    if songPath:
        say(f"Playing {song.capitalize()}...")
        os.system(f"open '{songPath}'")  
    else:
        say(f"I don't have the song {song}.")
