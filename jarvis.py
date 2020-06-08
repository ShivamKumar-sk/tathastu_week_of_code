import webbrowser as wb
import speech_recognition as sr
from tkinter import *
from time import ctime
import time
import os
from gtts import gTTS
import pygame
from pygame import mixer
from threadpoolctl import threadpool_info

def speak(audioString):
    global x
    b=audioString
    if len(b)==0:
        return
    tts=gTTS(text=b,lang='en-us')
    tts.save('voice%s.mp3'%(x))
    pygame.init()
    pygame.display.set_mode((2,1))
    mixer.music.load('voice%s.mp3'%(x))
    mixer.music.play(0)
    x+=1
    clock=pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)


def recordaudio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('speak....')
        audio=r.listen(source)
        print('heard..waiting for google to recognize audio')
    data=''
    try:
        data=r.recognize_google(audio)
        print('You said :',+data)
    except sr.UnknownValueError:
        print('Google could not understand what you said')
    except sr.RequestError as e:
        print('could not reques results from google speech recognition service;{0}'.format(e))
    return data

def jarvis(data):
    if 'how are you' in data:
        speak('I am fine')
    elif 'what time is it' in data:
        speak(ctime())
    elif 'where is' in data:
        data=data.split(" ")
        location=data[2]
        speak('hold on buddy, i will tell you where'+location+'is,')
        wb.open('https://www.google.com/maps/place/'+location)
    elif 'play video' in data:
        data=data.split(" ")
        video=data[2:]
        wb.open('https://www.youtube.com/results?search_query='+video)
        
    else:
        speak('i did not get what are you saying')
        
time.sleep(0.5)              
x=0
print('Start..')
speak('Hi! buddy what can i do for you?')
data=recordaudio()
jarvis(data)
speak('Turning off the program...')
print('completed..')
