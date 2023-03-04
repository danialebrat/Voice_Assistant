import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

newVoiceRate = 160

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', newVoiceRate)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)

    if "hello" in command.lower():
        talk("Hello there!")

    elif "how are you" in command.lower():
        talk("I'm fine, thank you.")

    elif "your name" in command.lower():
        talk("My name is Alex, it is pleasure to meet you. I'm like the alexa's older brother. But, I'm not as intelligence as her")

    elif "play music" in command.lower():
        talk("What song would you like me to play?")
        song_name = take_command()
        if song_name:
            talk(f"Playing {song_name}.")
            pywhatkit.playonyt(song_name)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif "youtube" in command.lower():
        talk("What would you like me to find on YouTube?")
        search_term = take_command()
        if search_term:
            talk(f"Searching YouTube for {search_term}.")
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_term}")

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'learn' in command:
        talk('They will learn so much exciting things about Artificial Intelligence, and they will learn how to build me!')

    elif 'any other projects' in command:
        talk('It depends on their speed! they can learn how to create an AI that solves soduku, and also exciting snake game, or even better, reverse snake GAME!')

    elif 'goodbye Alex' in command:
        talk('No worries, It was my pleasure to be a part of this trial session. I wish the good luck for all the students.')

    else:
        talk('please say the command again')

while True:
    run_alexa()






"""

Let's learn all about AI

"""












