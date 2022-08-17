from genericpath import exists
from random import random
from re import S, T

from unicodedata import name
from pip import main
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voices = engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Night")
    speak("I am Jarvis Sir, please tell me how can I help you")

def gamePlay():
    speak("Lets playyyy")
    i = 0
    my_score = 0
    com_score = 0

    while i <6:
        choose = ("rock", "paper", "scissors")
        com_choice = random.choice(choose)
        query = takeCommand().lower()

        if (query == com_choice):
            continue
        elif (query== "1") and (com_choice== "scissors"):
            my_score +=1
            speak(f"You won Sir, your score is {my_score}")
        elif (query == "2" and com_choice == "rock"):
            my_score +=1
            speak(f"You won Sir, your score is {my_score}" )
        elif (query == "3") and (com_choice == "paper"):
            my_score +=1
            speak(f"You won Sir, your score is {my_score} ")
        else:
            com_score +=1
            speak(f"I won huehuehue, my score is {com_score}" )

        i +=1
    if com_score >= my_score:
        speak("I defeated you sir, how are you feeling")
    else:
        speak("you cheated sir, I can nor be defeated")

def takeCommand():
    '''
    it takes microphone input from the user and return string
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")

        return "None"
    return query

if __name__ == "__main__":
    speak("hello sourav")
    wishMe()
    # takeCommand()

    while True:
    # if 1:
        query = takeCommand().lower()
        chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'   
        if 'wikipedia' in query:
            speak('Searching wikipedia...') 
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open_new("youtube.com")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'facebook' in query:
            webbrowser.open("facebook.com")
        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            n = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[n]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(strTime)

        elif 'web whatsapp' in query:
            webbrowser.get(chrome).open("webwhatsapp.com")

        elif 'vs code' in query:
            vsdir = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsdir)

        elif 'game' in query:
            # from rpsGame import gamePlay
            gamePlay()

        elif 'set alarm' in query:
            speak("Sir tell me the time when you wana wake up! like 5:30 am")
            alarm_time = takeCommand()
            alarm_time = alarm_time.replace("set alarm to ", " ")
            alarm_time = alarm_time.replace(".", " ")
            alarm_time = alarm_time.upper()
            import myalarm 
#             this func needs further rectification, showing bugs

            myalarm.myAlarm(alarm_time)

        elif 'quit' in query:
            exit()



