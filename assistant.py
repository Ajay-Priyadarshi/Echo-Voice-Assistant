# assistant.py

import re
import time

from data.websites import WEBSITES  
from data.applications import APPLICATIONS

from commands.websites import openWebsite
from commands.apps import openApplication
from commands.music import playMusic
from commands.utils import say, takeCommand, exitAssistant, handleFallback
from commands.system import updateSystem, changeVolume, setReminder, takeScreenshot, setBrightness
from commands.dateTime import tellTime, tellMonth, tellDate, tellDay, tellYear 
from commands.health import calculateBMI
from commands.news import getNews
from commands.weather import getWeather
from commands.jokes import tellJoke

# Import the global state
from commands.utils import is_awake as global_is_awake

# Common function to open websites and apps
def openSomething(target):
    targetLower = target.lower()
    if targetLower in WEBSITES:
        openWebsite(targetLower)
    elif targetLower in APPLICATIONS:
        openApplication(targetLower)
    else:
        say(f"I don't recognize {target} as an application or website.")


# Command Handler
def handleCommand(query):
    if "set reminder" in query:
        try:
            parts = query.split(" ", 3)  # Split into parts
            if len(parts) >= 4:
                time_part = parts[2]  
                message = parts[3] if len(parts) > 3 else "Reminder"  
                setReminder(time_part, message)
            else:
                say("Please provide both time and reminder message.")
        except Exception as e:
            say(f"Sorry, couldn't set the reminder: {str(e)}")
        return

    commands = {
        r'\bopen (.+)\b': openSomething,
        r'\bplay (.+)\b': playMusic,
        r'\bupdate the system\b': updateSystem,
        r'\bweather in (.+)\b': lambda city: say(getWeather(city)),
        r'\bnews\b': lambda: say(getNews()),
        r'\bjoke?\b': lambda: tellJoke(),
        r'\bvolume (increase|decrease|mute|unmute)\b': lambda action: changeVolume(action),
        r'\b(increase|decrease|mute|unmute) volume\b': lambda action: changeVolume(action),
        r'\bcalculate bmi\b' : lambda: calculateBMI(),
        r'\btake screenshot\b' : lambda: takeScreenshot(),
        r'\bset brightness to \d+%\b': lambda query: setBrightness(query),
        r'\bthe time\b': tellTime,
        r'\bthe day\b': tellDay,
        r'\bthe date\b': tellDate,
        r'\bthe month\b': tellMonth,
        r'\bthe year\b': tellYear,
        r'\byou can go\b': exitAssistant
    }

    # Check for each command pattern
    for pattern, func in commands.items():
        match = re.search(pattern, query)
        if match:
            if isinstance(func, type(lambda: 0)):  
                func(*match.groups())
            else:
                func(*match.groups())
            return
    handleFallback(query)


def main():
    global global_is_awake
    say("Hello, I am echo what can i do for you.")
    
    while True:
        if global_is_awake:
            query = takeCommand().lower()  
            if query:
                # Handle commands
                handleCommand(query)
                # Additional commands to change state
                if "sleep" in query or "go to sleep" in query:
                    say("Going to sleep.")
                    global_is_awake = False
            else:
                # No input detected, enter sleep mode
                global_is_awake = False
        else:
            # Asleep mode: listen only for wake-up command
            print("Assistant is asleep. Listening for wake-up command...")
            wake_command = takeCommand(listen_for_wake=True)
            if wake_command:
                if "wake up" in wake_command:
                    say("I'm awake.")
                    global_is_awake = True
                else:
                    say("Currently asleep give wake up commad to proceed.")
                    print("Ignoring command while asleep.")
            else:
                time.sleep(2)

if __name__ == '__main__':
    main()
