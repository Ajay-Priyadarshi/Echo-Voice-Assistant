# News commands

import requests
from config import NEWS_API_KEY

def getNews():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json()['articles'][:5]
        news = "Here are the top news headlines: "
        for article in articles:
            news += article['title'] + ". "
        return news
    else:
        return "I couldn't retrieve the news at the moment."