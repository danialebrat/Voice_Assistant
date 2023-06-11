"""
pip install SpeechRecognition
pip install pyttsx3
pip install pywhatkit
pip install wikipedia
pip install pyjokes



"""





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
            return command
    except:
        print("repeat the question again")


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

    elif 'time' in command.lower():
        time = datetime.datetime.now()
        talk('Current time is ' + time)


    elif "youtube" in command.lower():
        talk("What would you like me to find on YouTube?")
        search_term = take_command()
        if search_term:
            talk(f"Searching YouTube for {search_term}.")
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_term}")

    # Access wikipedia
    elif 'wikipedia' in command.lower():
        talk('searching wekipedia...')
        query = command.replace('wikipedia', '')
        result = wikipedia.summary(query, sentences=2)
        print(result)
        talk(result)

    # Access Google
    elif 'google ' in command.lower():
        webbrowser.open('https://www.google.com/')

    # Access mail inbox
    elif 'mail' in command.lower() or 'Gmail' in command.lower():
        webbrowser.open('https://mail.google.com/')

    elif 'joke' in command.lower():
        talk(pyjokes.get_joke())

    else:
        talk('please say the command again')

if __name__ == "__main__":

    while True:
        run_alexa()






"""

Let's learn all about AI

"""












