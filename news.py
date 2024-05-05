import pyttsx3
import requests
import json


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def latesnews():
    apidict = {"bussiness":'https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=5323daf1485c4ff3a6ee1eb73c0f32e5',
              "health":'https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=5323daf1485c4ff3a6ee1eb73c0f32e5'}
    

    content = None
    url = None
    speak("which feild news do you want, [bussiness],[health]")
    field = input("Type field news that you want: ")
    for key,values in apidict.items():
        if key.lower() in field.lower():
            url = values
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
                print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news")

    arts = news["articles"]
    for articles in arts:
        article = articles['title']
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit:{news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
        speak("thats all")
