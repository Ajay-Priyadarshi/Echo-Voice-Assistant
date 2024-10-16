# Time and Date Functions

from datetime import datetime
from commands.utils import (say)

def tellTime():
    current_time = datetime.now().strftime("%H:%M:%S")
    say(f"The time is {current_time}")

def tellDay():
    current_day = datetime.now().strftime("%A")
    say(f"Today is {current_day}")

def tellDate():
    current_date = datetime.now().strftime("%d")
    say(f"Today's date is {current_date}")

def tellMonth():
    current_month = datetime.now().strftime("%B")
    say(f"The current month is {current_month}")

def tellYear():
    current_year = datetime.now().strftime("%Y")
    say(f"The current year is {current_year}")