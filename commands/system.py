# commands/system.py

import os
import threading
import datetime
import subprocess
from plyer import notification
from commands.utils import say

reminders = {}

def updateSystem():
    say("Updating the system...")
    os.system("sudo apt update && sudo apt upgrade -y")

def changeVolume(action):
    if action == "increase":
        os.system("amixer -D pulse sset Master 5%+")
        say("Volume increased")
    elif action == "decrease":
        os.system("amixer -D pulse sset Master 5%-")
        say("Volume decreased")
    elif action == "mute":
        os.system("amixer -D pulse sset Master mute")
        say("Volume muted")
    elif action == "unmute":
        os.system("amixer -D pulse sset Master unmute")
        say("Volume unmuted")

def setReminder(time, message):
    try:
        reminderTime = datetime.datetime.strptime(time, "%H:%M")
        now = datetime.datetime.now()
        reminderTime = reminderTime.replace(year=now.year, month=now.month, day=now.day)
        if reminderTime < now:
            reminderTime += datetime.timedelta(days=1)  # Move to next day if time has already passed today
        
        difference = (reminderTime - now).total_seconds()
        # Set the reminder using threading
        threading.Timer(difference, lambda: sendNotification(message)).start()
        reminders[time] = message
        say(f"Reminder set for {time}")

    except ValueError as ve:
        say(f"Invalid time format: {str(ve)}")
    except Exception as e:
        say(f"Failed to set reminder: {str(e)}")

def sendNotification(message):
    notification.notify(
        title="Voice-Assistant",
        message=message,
        timeout=10  
    )

def takeScreenshot():
    subprocess.run(['scrot','/home/ryuk/Pictures/screenshot_%Y-%m-%d_%H:%M:%S.png']) # path to ss directory
    print("Screenshot taken")
    say("Screenshot taken")

def setBrightness(level):
    try:
        level = int(level)  
        if 0 <= level <= 100:
            # Fetch the display name dynamically
            output = subprocess.check_output(['xrandr']).decode('utf-8')
            display_name = None
            
            for line in output.splitlines():
                if " connected" in line:
                    display_name = line.split()[0]  # Get the display name
                    break
            
            if display_name:
                brightness_value = level / 100  
                subprocess.run(['xrandr', '--output', display_name, '--brightness', str(brightness_value)], check=True)
                say(f"Brightness set to {level}%.")
            else:
                say("Could not determine the display name.")
        else:
            say("Please provide a brightness level between 0 and 100%.")
    except ValueError:
        say("Invalid brightness level. Please provide a number between 0 and 100.")
    except subprocess.CalledProcessError:
        say("Failed to set brightness. Please ensure xrandr is installed and configured correctly.")
    except Exception as e:
        say(f"An error occurred: {str(e)}")
