# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:21:44 2020

@author: Pranav
"""
import json
import time
def getnews():
    import requests
    r = requests.get('http://newsapi.org/v2/top-headlines?country=in&apiKey=d112b7c47ef34f4bba02f35c5c783670')
    a=r.text
    parsed = json.loads(a)
    par_art=parsed['articles']
    return par_art
def speak(content):
    from win32com.client import Dispatch
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(content)
if __name__ == '__main__':  
    print("News Reader")
    name=input("Enter Your name\n")
    nn=int(input('How many news you want to see 1-10\n'))
    
    if time.strftime('%H') >= str(6) and time.strftime('%H') < str(12):
        speak(f"Good Morning {name}")
    elif time.strftime('%H') >= str(12) and time.strftime('%H') < str(17):
        speak(f"Good Afternoon {name}")
    elif time.strftime('%H') >= str(17) and time.strftime('%H') < str(20):
        speak(f"Good Evening {name}")
    else :
        speak(f"Good Night{name}")    
    speak(f'Here are the top {nn} news') 
    gn_di=getnews()
    for i in range(1,nn+1):
        speak(f'News number {i}')
        time.sleep(1)
        speak('Title')
        print('\nTitle\n',(gn_di[i]['title']))
        speak(gn_di[i]['title'])
        time.sleep(1)
        speak('Content')
        txt=gn_di[i]['content']
        print('\nContent\n',txt)
        speak(txt)
