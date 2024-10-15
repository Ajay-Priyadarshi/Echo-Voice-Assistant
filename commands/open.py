import os
import webbrowser
from commands.utils import say
from data.applications import APPLICATIONS
from data.websites import WEBSITES  

def openApplication(app):
    appCommand = APPLICATIONS.get(app.lower())
    if appCommand:
        say(f"Opening {app.capitalize()}...")
        os.system(appCommand)
    else:
        say(f"I don't recognize the application {app}.")


def openWebsite(site_name):
    url = WEBSITES.get(site_name.lower())
    if url:
        say(f"Opening {site_name.capitalize()}...")
        webbrowser.open(url)
    else:
        say(f"I don't recognize the website {site_name}.")
