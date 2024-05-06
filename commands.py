import requests
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia as wi
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyaudio
from os import close, system
from PyQt5.QtCore import *
from wikipedia.wikipedia import search
import pyjokes
import pyautogui
from pyautogui import KEYBOARD_KEYS, click, press
import os.path
from os import close , system

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[len(voices) - 1].id)

# Making function that our assistant can speak and wait to hear our text:
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# For receiving information to user:
def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language='en-in')
        print(f"user said: {text}\n")

    except Exception as e:
        speak("Say that again")
        return "none"
    return text

# making function that when its run he greets first and then run our program
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morning sir")
    elif hour >= 12 and hour <= 18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("please tell me how may i help you")

if __name__ == "__main__": # Main program
    wish()
    while True:
        text = takecommand().lower()

# To build logic for tasks:
        if "open notepad" in text:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'hi' in text or 'hello' in text:
            speak('Hello sir, how may I help you?')

        elif "open command prompt" in text:
            os.system("start cmd")

        elif "open camera" in text:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

# To shut down assistant:
        elif 'terminate' in text:
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour <= 12:
                speak("OK sir, have a nice day")
                sys.exit()
            elif hour >= 12 and hour <= 18:
                speak("OK sir, have a nice day")
                sys.exit()
            else:
                speak("OK sir, good night")
                sys.exit()


# For getting info from Wikipedia:
        elif "wikipedia" in text:
            speak("searching wikipedia...")
            text = text.replace("wikipedia","")
            result = wi.summary(text, sentences = 2)
            speak("according to wikipedia")
            speak(result)


# Getting time from assistant:
        elif "what's the time" in text:
            strftime = datetime.datetime.now().strftime("%H %M")
            print(strftime)
            speak(F"sir, the time is{strftime}")

# For showing ip address:
        elif "ip address" in text:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

# For opening Youtube:
        elif "open youtube" in text:
            webbrowser.open("www.youtube.com")

# For opening facebook:
        elif "open facebook" in text:
            webbrowser.open("www.facebook.com")

# for opening stackoverflow
        elif "open stack overflow" in text:
            webbrowser.open("www.stackoverflow.com")

# For opening Telegram:
        elif "open telegram" in text:
            webbrowser.open("https://web.telegram.org//a//")

# For opening Google:
        elif "open google" in text:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

# To open Whatsapp in browser:
        elif "open whatsapp" in text:
            webbrowser.open("https://web.whatsapp.com/")
            speak("ok sir, opening whatsapp web")

# For sending message on Whatsapp:
        elif 'send message on whatsapp' in text:
            speak("tell me the name of the person!")
            text = takecommand().lower()
            if 'aditya' in text:
                speak("tell me message!")
                msg = takecommand().lower()
                kit.sendwhatmsg_instantly("+917623967294",msg)
                speak("ok sir, sending whatsapp message !")
                click(x=1787, y=972)
                speak("message has been sent")

# For listening particular song on youtube:
        elif "song on youtube" in text:
            kit.playonyt("Andrew Garfield Original Clip 4K60fps | Kali Uchis - Moonlight (I just wanna get high with my lover)")

# For setting a timer or using a stopwatch:
        elif 'timer' in text or 'stopwatch' in text:
            speak("For how many minutes?")
            timing = takecommand()
            timing = timing.replace('minutes', '')
            timing = timing.replace('minute', '')
            timing = timing.replace('for', '')
            timing = float(timing)
            timing = timing * 60
            speak(f'I will remind you in {timing} seconds')
            time.sleep(timing)
            speak('Your time has been finished sir')

# For 
        elif "no thanks" in text:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

# To close any application:
        elif "close notepad" in text:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

# To set an alarm:
        elif "set alarm" in text:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = 'E:\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

# To find a joke:
        elif "tell me a joke" in text:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in text:
            os.system("shutdown /s /t 5")

        elif "restart the system" in text:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in text:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

# Switching windows:
        elif 'switch the window' in text:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
