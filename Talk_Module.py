import  pyttsx3

coco=pyttsx3.init()

def Speak_Funtion(command):
    coco.say(command)
    coco.runAndWait()