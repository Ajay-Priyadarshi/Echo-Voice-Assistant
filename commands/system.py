# commands/system.py

import os
import threading
import datetime
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
        timeout=10  # Notification duration in seconds
    )