
import webbrowser
from commands.utils import say
from data.websites import WEBSITES  # Absolute import

def openWebsite(site_name):
    url = WEBSITES.get(site_name.lower())
    if url:
        say(f"Opening {site_name.capitalize()}...")
        webbrowser.open(url)
    else:
        say(f"I don't recognize the website {site_name}.")
