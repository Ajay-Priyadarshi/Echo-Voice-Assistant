import speech_recognition as sr
import os

# State variable to track if the assistant is awake
is_awake = True

def say(text):
    safeText = text.replace('"', '\\"').replace("'", "\\'")
    os.system(f'espeak "{safeText}"')

def takeCommand(listen_for_wake=False):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        if not listen_for_wake:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")  # Active listening message
        else:
            # Optional: Adjust parameters for wake word detection if needed
            recognizer.pause_threshold = 1
            print("Listening for wake command...")  # Distinct message for sleep mode

        try:
            if listen_for_wake:
                # Timeout for wake word detection
                audio = recognizer.listen(source, timeout=5000, phrase_time_limit=5000)  # 10 seconds for wake word detection
            else:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)  # Shorter timeout for active listening
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
