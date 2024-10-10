# commands/__init__.py

from commands.websites import openWebsite
from commands.apps import openApplication
from commands.music import playMusic
from commands.utils import say,takeCommand, exitAssistant, handleFallback
from commands.system import updateSystem, changeVolume, setReminder
from commands.dateTime import tellTime, tellMonth, tellDate, tellDay, tellYear 
from commands.news import getNews
from commands.weather import getWeather
