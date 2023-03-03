import speech_recognition as sr
import pyttsx3
import datetime

# initialize the recognizer and engine
r = sr.Recognizer()
engine = pyttsx3.init()

# define a function to take voice input and convert it to text
def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print("You said: " + command)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            command = None
        return command

# define a function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# main program loop
while True:
    command = take_command()
    if command:
        if "hello" in command.lower():
            speak("Hello there!")
        elif "how are you" in command.lower():
            speak("I'm fine, thank you.")
        elif "what time is it" in command.lower():
            speak("It is currently " + datetime.datetime.now().strftime("%I:%M %p"))
        elif "goodbye" in command.lower():
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I don't understand.")