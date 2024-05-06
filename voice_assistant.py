import pyttsx3
import speech_recognition as sr
from transformers import pipeline
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia as wi
import webbrowser
import pywhatkit as kit
import sys
import time
from os import close, system
from PyQt5.QtCore import *
from wikipedia.wikipedia import search
import pyjokes
import pyautogui
from pyautogui import KEYBOARD_KEYS, click
import os.path

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the text generation pipeline with the GPT-2 model
generator = pipeline("text-generation", model="gpt2")

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print("Skipping unknown error")

def generate_response(prompt):
    # Generate text based on the prompt
    response = generator(prompt, max_length=100, num_return_sequences=1, do_sample=True)[0]['generated_text']
    return response

def filter_response(response):
    # Remove irrelevant parts from the response
    filtered_response = "\n".join(response.split("\n")[:2])  # Keep the first two lines
    return filtered_response

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def  takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

def main():
    
    while True:
        # Wait for user to say "Cypher" or "Terminate"
        print("Say 'Cypher' to start recording your question or 'Terminate' to exit...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "cypher":
                    # Record audio
                    filename = "input.wav"
                    print("Ask your question...")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    # Transcribe audio to text
                    text = transcribe_audio_to_text(filename)

                    if text:
                        print(f"You said: {text}")

                        # To build logic for tasks:
                        if "open Notepad" in text:
                            npath = r"C:\Windows\notepad.exe"
                            os.startfile(npath)

                        elif 'hi' in text or 'hello' in text:
                            speak_text('Hello sir, how may I help you?')

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
                                speak_text("OK sir, have a nice day")
                                sys.exit()
                            elif hour >= 12 and hour <= 18:
                                speak_text("OK sir, have a nice day")
                                sys.exit()
                            else:
                                speak_text("OK sir, good night")
                                sys.exit()

                        # For getting info from Wikipedia:
                        elif "Wikipedia" in text:
                            speak_text("searching wikipedia...")
                            text = text.replace("wikipedia","")
                            result = wi.summary(text, sentences = 2)
                            speak_text("according to wikipedia")
                            speak_text(result)

                        # Getting time from assistant:
                        elif "what's the time" in text:
                            strftime = datetime.datetime.now().strftime("%H %M")
                            print(strftime)
                            speak_text(F"sir, the time is{strftime}")

                        # For showing ip address:
                        elif "IP address" in text:
                            ip = get('https://api.ipify.org').text
                            speak_text(f"your IP address is {ip}")

                        # For opening Youtube:
                        elif "open YouTube" in text:
                            webbrowser.open("www.youtube.com")

                        # For opening facebook:
                        elif "open Facebook" in text:
                            webbrowser.open("www.facebook.com")

                        # for opening stackoverflow
                        elif "open stack overflow" in text:
                            webbrowser.open("www.stackoverflow.com")

                        # For opening Telegram:
                        elif "open telegram" in text:
                            webbrowser.open("https://web.telegram.org//a//")

                        # For opening Google:
                        elif "open Google" in text:
                            speak_text("sir, what should i search on google")
                            cm = takecommand().lower()
                            webbrowser.open(f"{cm}")

                        # To open Whatsapp in browser:
                        elif "open WhatsApp" in text:
                            webbrowser.open("https://web.whatsapp.com/")
                            speak_text("ok sir, opening whatsapp web")

                        # For sending message on Whatsapp:
                        elif 'send message on WhatsApp' in text:
                            speak_text("tell me the name of the person!")
                            text = takecommand().lower()
                            if 'aditya' in text:
                                speak_text("tell me message!")
                                msg = takecommand().lower()
                                kit.sendwhatmsg_instantly("+917623967294",msg)
                                speak_text("ok sir, sending whatsapp message !")
                                click(x=1787, y=972)
                                speak_text("message has been sent")

                        # For listening particular song on youtube:
                        elif "song on YouTube" in text:
                            kit.playonyt("Valorant - Official Cypher Theme Song (Hyume - Confused) - Riot Games")

                        # For setting a timer or using a stopwatch:
                        elif 'timer' in text or 'stopwatch' in text:
                            speak_text("For how many minutes?")
                            timing = takecommand()
                            if timing:
                                timing = timing.replace('minutes', '')
                                timing = timing.replace('minute', '')
                                timing = timing.replace('for', '')
                                timing = float(timing)
                                timing = timing * 60
                                speak_text(f'I will remind you in {timing} seconds')
                                time.sleep(timing)
                                speak_text('Your time has finished, sir.')
                            else:
                                speak_text("I'm sorry, I didn't catch that. Could you please repeat?")

                        # For terminating the program:
                        elif "no thanks" in text:
                            speak_text("thanks for using me sir, have a good day.")
                            sys.exit()

                        # To close any application:
                        elif "close notepad" in text:
                            speak_text("okay sir, closing notepad")
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
                            speak_text(joke)

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

                        # Generate response using GPT-2
                        else:
                            response = generate_response(text)
                            print(f"Cypher says: {response}")
                            # Filter response
                            filtered_response = filter_response(response)
                            print(f"Filtered response: {filtered_response}")
                            # Read response using text-to-speech
                            speak_text(filtered_response)

                elif transcription.lower() == "terminate":
                    print("Terminating program...")
                    break  # exit the loop and terminate the program

            except Exception as e:
                print("An error occurred: No input!", format(e))

if __name__ == "__main__":
    main()