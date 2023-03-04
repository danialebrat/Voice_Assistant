'''
Necessary pip installation requires are

  1. pip install pyttsx3
  2. pip install speechRecognition
  3. pip install wikipedia
  4. pip install webbrowser
  5. pip install pipwin
  6. pip install PyAudio


'''

import pyttsx3
import speech_recognition as sr
import datetime
import sys
import wikipedia
import webbrowser
import os
import random
import string

# To take voice as user input we are using pyttsx3 and sapi5

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# voices[0] and voices[1] are the available voice in pyttsx3
engine.setProperty('voice', voices[0].id)


# This function is used to speak or read the result you give as audio

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# wishme function to wish the welcome (good morning) according to time
def wishme():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak('Good morning! Sir')
    elif hour >= 12 and hour < 17:
        speak('good afternoon!')
    else:
        speak('good evening!')
    speak('please let me know the  commands for me.')


def takeCommand():
    ## take microphhone inputand   return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        audio = r.listen(source)
        print('stoped listening.')
    try:
        print('recognizing...')

        # goole recognize is used to convert audio in to string
        query = r.recognize_google(audio)
        print('you said: ', query)

    except:
        print('say it again please.')
        return 'None'

    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        # Access wikipedia
        if 'wikipedia' in query:
            speak('searching wekipedia...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        # Access youtube
        elif ' youtube ' in query:
            webbrowser.open('https://www.youtube.com/')

        # Access Google
        elif 'google ' in query:
            webbrowser.open('https://www.google.com/')

        # Access Music playing from jiosaavn
        elif 'play music' in query or 'song' in query:
            webbrowser.open('https://www.jiosaavn.com/')

            # Shut down this pc saying shut down while working
        elif 'shutdown' in query or 'shut down' in query:
            speak('Do you really wanna shut down you PC')
            what = input('Yes/No')
            n = input()
            if n == 'n' or n == 'N' or n == 'NO' or n == 'no':
                speak('No problem! Enjoy your work')
            elif n == 'y' or n == 'yes' or n == 'Y' or n == 'YES':
                os.system('shutdown /s /t 1')


        # Access mail inbox
        elif 'mail' in query or 'Gmail' in query:
            webbrowser.open('https://mail.google.com/')

            # Stack-over flow access
        elif 'stack overflow' in query:
            webbrowser.open('www.stackoverflow.com')

        # Tell me the time right now
        elif 'time' in query:
            d = datetime.datetime.now().strftime('%H:%M:%S')
            speak('Time now is');
            speak(d)

        # Know the date
        elif 'date' in query:
            d = datetime.datetime.now()
            month = [
                'january', 'february', 'march', 'april', 'may', 'june',
                'july', 'august', 'september', 'october', 'november', 'december'
            ]

            s = str(d.day) + ' ' + str(month[(d.month) - 1]) + ' ' + str(d.year)
            speak(s)

