#pip install secure-smtplib
#pip install pyttsx3
#pip install playsound
#pip install pyAudio

import smtplib
import speech_recognition as sr
from email.message import EmailMessage
import pyttsx3


listenser=sr.Recognizer()

textToSpeech=pyttsx3.Engine()

def talking(text):
	textToSpeech.say(text)
	textToSpeech.runAndWait()



def microPhone():
	with sr.Microphone() as source:
		print("Program is listening.....")
		voice=listenser.listen(source)
		data = listenser.recognize_google(voice)
		print(data)
		return data.lower()

dict = {"jojo":"abhijitmajumder906@gmail.com"}

def sendMail(receiver,subject,body):
	server = smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login("majumderabhijit28@gmail.com","rkau")
	email=EmailMessage()
	email["From"]="majumderabhijit28@gmail.com"
	email["To"]=receiver
	email["Subject"]=subject
	email.set_content(body)
	server.send_message(email)

def mainFuntion():
	talking("To whom do you want to send the email enter? ")
	name = input("Enter Email: ")
	receiver= name
	talking("The subject of your Email: ")
	subject=microPhone()
	talking("Speak the body of the Email: ")
	body=microPhone()
	sendMail(receiver,subject,body)
	print("Your Email has been sent!!!!")
