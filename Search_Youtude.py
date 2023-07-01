import pywhatkit
import wikipedia
from Time_Module import Speak_Funtion

def searchSong(command):
    return pywhatkit.playonyt(command)

def Search_Web(command):
    return pywhatkit.search(command)

def Summary(command):
    info=wikipedia.summary(command,1)
    Speak_Funtion(info)
    return info

