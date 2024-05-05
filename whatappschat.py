import pyttsx3
import datetime
import pyautogui
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta,datetime
import speech_recognition as sr
import pywhatkit

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
 

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
        print(f"You said: {query}\n")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Could you please repeat?")
        return "None"
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes=2)).strftime("%M"))

def sendMessage():
    speak("Who do you want to msg")
    a = int( input('''person 1 - 1
              person 2 - 2
              person 3 - 3'''))
    if a == 1:
        speak("whats the message")
        message = takecommand()
        print(message)
        speak (f"okay i will be send msg {message}")
        pywhatkit.sendwhatmsg("+918780928112",message,time_hour=strTime,time_min=update)
    elif a == 2:   
        speak("whats the message")
        message = str(input("Enter the message-"))
        pywhatkit.sendwhatmsg("+919687825353",message,time_hour=strTime,time_min=update)