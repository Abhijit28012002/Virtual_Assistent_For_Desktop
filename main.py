import speech_recognition as sr
import pyttsx3
from Search_Youtude import searchSong,Search_Web,Summary
from Time_Module import get_Time
from PhoneNumber import Country_Pro
from Send_Email import mainFuntion


listener=sr.Recognizer()
coco=pyttsx3.init()
voices=coco.getProperty('voices')
coco.setProperty('voice',voices[1].id)
coco.say("Welcome I am Coco Your virtual assistent")
coco.runAndWait()
print("\t\t\t\t\tWelcome I am Coco Your virtual Assistent")
print("\t\t\t\t\t----------------------------------------")


while True:
    with sr.Microphone() as source:
        coco.say("I am Listening")
        coco.runAndWait()
        print("I am Listening.....")
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        print(command)
        command=command.lower()
        if 'play song' in command or 'play music' in command:
            searchSong(command)
            input()
        elif 'search' in command:
            Search_Web(command)
            input()
        elif 'send email' in command:
            mainFuntion()
        elif 'phone number' in command:
            coco.say("Enter your mobile number")
            coco.runAndWait()
            Country_Pro()
        elif 'summary' in command:
            command=command.replace('summary','')
            d=Summary(command)
            print(d)
        elif 'time' in command:
            time=get_Time()
            print(time)
        elif 'exit' in command:
            break
        else:
            coco.say("Choose valid options")
            coco.runAndWait()


