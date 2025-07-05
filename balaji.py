from math import e
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import smtplib


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[0].id) 
engine.setProperty('voice', voices[0].id)  

def speak(audio):
    engine.say(audio)  
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("HELLO SUMIT Sir  I AM JARVIS, HOW MAY I HELP YOU")


def takecommand():
    # it takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:  
        print("Recognising..")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said:{query}\n")  
    except Exception as e: 
        print(e)
        print("say that again please")
        return "None" 

    return query


# (if_name_=="_main_":)  

speak("Jay Shree Ram")
wishMe()
query=takecommand().lower()



#logic for executing task based on query



if 'wikipedia' in "query":
    speak=("searching wikipedia..")
    query= query.replace("wikipedia", "")
    results=wikipedia.summary(query ,sentence=2)
    speak=("according to wikipedia")
    print (results)
    speak (results)

elif 'open youtube'in query:
    webbrowser.open("youtube.com")

elif 'open whatsapp'in query:
    webbrowser.open("whatsapp.com")

elif 'open google'in query:
    webbrowser.open("google.com")

elif 'open wikipedia'in query:
    webbrowser.open("wikipedia.com")
    
    
elif 'the time'in query:
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is{strTime}")
    



