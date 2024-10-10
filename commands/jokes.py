import requests
from commands.utils import say

def tellJoke():
    url = "https://v2.jokeapi.dev/joke/Any?type=single"  
    try:
        response = requests.get(url)
        response.raise_for_status()  
        jokeData = response.json()
        
        if jokeData['error']:
            say("Oops, I couldn't find a joke right now.")
            return
        
        if jokeData['type'] == 'single':
            joke = jokeData['joke']
        else:
            joke = f"{jokeData['setup']} ... {jokeData['delivery']}"
        
        say(joke)
    
    except requests.exceptions.RequestException as e:
        say("Sorry, I'm having trouble connecting to the joke service.")
        print(f"Error fetching joke: {e}")
