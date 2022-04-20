import pyttsx3          # text-to-speech conversion library,works offline as well
import speech_recognition as sr     
import smtplib
from http import server
import os
from tkinter import EXCEPTION
from flask import request
import wikipedia
import webbrowser
import datetime
import cv2
import random
from requests import get
import pywhatkit as kit
import sys
import pyjokes
import pyautogui
import requests
import time



engine=pyttsx3.init('sapi5')        # sepi5 is for windows.for mac it is nsss
'''The pyttsx3 module supports two voices first is female and the second is male which is provided by “sapi5”'''
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

#Text to speech
def speak(audio):
    '''This function is for speak the text which is passed as parameter.'''
    engine.say(audio)
    # .say() method is used to speak the text which is passed as argument.
    engine.runAndWait()

def wishMe():
    '''This function is for greeting the user.It will run only first time.'''
    hour=int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("Good evening")
    speak("I am  Prototype 1,how may i help you ")

#To convert voice into text
def takeCommand():  
    '''This function is for recognizing the voice of user and converting it into text.'''    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=1
        #r.energy_threshold=200
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please")
        speak("Say that again please")
        return "None"
    return query

def  sendEmail(to, content):
    '''This function is for send e-mail to any person using smtplib module.'''
    server=smtplib.SMTP('smtp.gmail.com', 587)
    # here we are using gmail SMTP(Simple Mail Transfer Protocol) server port number is 587.
    server.ehlo()
    server.starttls()
    server.login('zakkiwork732.gmail.com','z@kkiworks786')      # very less secure.
    server.sendmail('zakkiwork732.gmail.com',to,content)
    # first parameter is sender-mailID, 
    # second parameter is reciever-mailID, 
    # third parameter is message which have to send.
    server.close()   

def news():
    #3801ee1289054d0b931574de41a92cd0
    main_url='http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3801ee1289054d0b931574de41a92cd0'
    main_page=requests.get(main_url).json() 
    #print(main_page)
    articles=main_page["articles"]
    #print(articles)
    head=[]
    day=["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        #print(f"Today's {day[i]} nes is: {head[i]}")
        speak(f"Today's {day[i]} news is: {head[i]}")
        
if __name__=="main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak("Sir,what should I search on google")
            gs=takeCommand().lower()
            webbrowser.open(f"{gs}")
       
        elif 'send message' in query:
            kit.sendwhatmsg("+918652336784","This message is send by Prototype 1",14,2)

        elif 'play song on youtube' in query:
            kit.playonyt("Excuses Ap Dhillon")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
       
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
       
        elif 'open whatsapp ' in query:
            webbrowser.open("whatsapp.com")
       
        elif 'open javatpoint' in query:
            webbrowser.open("javatpoint.com")
        
        elif 'ip address' in query:
            ip=get('https://api.ipify.org').text
            speak(f"{ip} is your ip Address")
            print(f"{ip} is your ip Address")

        elif 'open camera' in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(25)
                if k==10:
                    break
            cap.release()
            cv2.destroyAllWindows()


        elif 'tell me a joke ' in query:
            joke=pyjokes.get_jokes()
            speak(joke)

        elif 'tell me news' in query:
            speak('please wait sir, fetching the latest news')
            news()

        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'play music' in query:
            Music_dir='C:\\Users\\JK\\Music\\Fav'
            songs=os.listdir(Music_dir)
            rd=random.choice(songs)
            #print(songs)
            os.startfile(os.path.join(Music_dir,rd))
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir ,the time is{strTime}")

        elif 'open vs code' in query:
            codePath="C:\\Users\\JK\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open notepad' in query:
            codePath="C:\\Windows\\system32\\notepad.exe"
            os.startfile(codePath)

        elif 'close notepad' in query:
            speak("Okay sir,closing notepad")
            os.system("taskkill /f /im notepad.exe")
           
        elif 'set alarm' in query:
          alarm=int(datetime.datetime.now().hour)
          if alarm==22:
              music_dir='C:\\Users\\JK\\Music\\Fav'
              songs=os.listdir(music_dir)
              os.startfile(os.path.join(music_dir,songs[0]))  

        elif 'send email to ' in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                to="zakkiwork732@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry Sir im not able to send this Email currently")

        elif 'you can sleep' in query:
            speak("Thanks for using me sir,have a good day")
            print("Thanks for using me,have a good day")
            exit() 
        
        elif 'shutdown the system' in query:
            os.system("shutdown /s /t 5")

        
        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")