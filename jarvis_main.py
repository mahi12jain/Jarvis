import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup 
import datetime
import os
import pyautogui
import keyboard
import random
import webbrowser
from plyer import notification
from pygame import mixer
# for i in range(3):
#     a = input("enter password")
#     pw_file = open("password.txt","r")
#     pw = pw_file.read()
#     pw_file.close()
#     if(a == pw):
#         print("welcome Mem pls speak Wek Up Load me up")
#         break
#     elif(i==2 and a != pw):
#         exit()
#     elif(a != pw):
#         print("try again")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

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
       

def alarm(query):
    timehere = open("alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
   
        query = takecommand().lower()
        if "wake up" in query:
            from greetMe import greetMe
            greetMe()

            while True:
             
                query = takecommand().lower()
                if "go to sleep" in query:
                    speak("ok mem, you can call anytime")
                    break


                elif "change password" in query:
                    speak("what's the new password")
                    new_pw = input("Enter new password")
                    new_password = open("password.txt","w")

                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"your new password is {new_pw}")

                elif "schedule my day" in query:
                    tasks = [] #Empty list
                    speak("Do you want to clear old task pls speak yes no")
                    query = takecommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the number of tasks :-"))
                        i = 0
                        for i in range (no_tasks):
                            tasks.append(input("Enter the task :-"))
                            file = open("tasks.txt",'a')
                            file.write(f"{i}.{tasks[i]}\n")
                            file.close()

                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the number of tasks :-"))
                        for i in range (no_tasks):
                            tasks.append(input("Enter the task :-"))
                            file = open("tasks.txt",'a')
                            file.write(f"{i}.{tasks[i]}\n")
                            file.close()
                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )
                #####################################
                elif "hello" in query:
                    speak("Hello mem How are you?")
                elif "I am fine" in query:
                    speak("thats great mem")
                elif "how are you" in query:
                    speak("perfact mem")
                elif "thank you" in query:
                    speak("you are welcome ,mem")

                elif "tried" in query:
                    speak("playing your favouriate songs")
                    a = (1,2,3,4)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=Ruuz127h-MQ")

                elif "google" in query:
                    from searchNow import searchGoogle
                    searchGoogle(query)

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video mute")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down ,mem")
                    volumedown()

                elif "whatsapp" in query:
                    from whatappschat import sendMessage
                    sendMessage(1)

                elif "open" in query:
                    from Dict import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dict import closeappweb
                    closeappweb(query)

                elif "youtube" in query:
                    from searchNow import searchYoutube
                    searchYoutube(query)

                elif "wikpedia" in query:
                    from searchNow import searchWikipedia
                    searchWikipedia(query)

                # elif "news" in query:
                #     from

                elif "set an alarm" in query:
                    print("input time example : 10 and 10 and 10")
                    speak("set the time")
                    a = input("please tell the time :-")
                    alarm(a)
                    speak("Done ,mem")

                elif "temperature" in query:
                     search = "temperature in ahmedabad"
                     url = f"https://www.google.com/search?q={search}"
                     r = requests.get(url)
                     data = BeautifulSoup(r.text,"html.parser")            
                     temp = data.find("div", class_ = "BNeawe").text
                     speak (f" cureent {search} is {temp}")

                elif "weather" in query:
                     search = "temperature in ahmedabad"
                     url = f"https://www.google.com/search?q={search}"
                     r = requests.get(url)
                     data = BeautifulSoup(r.text,"html.parser")            
                     temp = data.find("div", class_ = "BNeawe").text
                     speak (f" cureent {search} is {temp}")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Mem, the time is {strTime}")

                elif "finally sleep" in query:
                    speak("Going to sleep,mem bye")
                    exit()
                
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me "+rememberMessage)
                    remember = open("remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                    
                elif "what do you remember" in query:
                    remember = open("remember.txt","r")
                    speak("you told me" + remember.read())

                elif "news" in query:
                    from news import latesnews
                    latesnews() 

                elif "i am very hungry" in query:
                    speak("what do you eat ?")

                elif "shutdown system" in query:
                    speak("Are you sure want to shutdown ")
                    shutdown = speak("Do you wish to shutdown your computer yes or no ?")
                    if shutdown == 'yes':
                        os.system("shutdown /s /t 1")

                    elif shutdown == 'no':
                        break                
