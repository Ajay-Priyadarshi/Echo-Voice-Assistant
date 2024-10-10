import os
from commands.utils import say
from data.applications import APPLICATIONS

def openApplication(app):
    appCommand = APPLICATIONS.get(app.lower())
    if appCommand:
        say(f"Opening {app.capitalize()}...")
        os.system(appCommand)
    else:
        say(f"I don't recognize the application {app}.")