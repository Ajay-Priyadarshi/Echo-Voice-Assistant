import speech_recognition as sr
import os

is_awake = True

def say(text):
    safeText = text.replace('"', '\\"').replace("'", "\\'")
    os.system(f'espeak "{safeText}"')

def takeCommand(listen_for_wake=False):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        if not listen_for_wake:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")  
        else:
            recognizer.pause_threshold = 1
            print("Listening for wake command...")  

        try:
            if listen_for_wake:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)  
            else:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)  
        except sr.WaitTimeoutError:
            return ""

    try:
        query = recognizer.recognize_google(audio, language="en-in").lower()
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        if not listen_for_wake:
            print("Sorry, I did not hear that.")
            say("Sorry, I did not hear that.")
        return ""  
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        say("Could not request results; check your network connection.")
        return ""  

def exitAssistant():
    say("Echo out.")
    exit()

def handleFallback(query):
    say("I did not understand that command.")
