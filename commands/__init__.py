# commands/__init__.py

from commands.open import openApplication, openWebsite
from commands.music import playMusic
from commands.utils import say, setVoice, takeCommand, exitAssistant, handleFallback
from commands.system import updateSystem, changeVolume, setReminder, takeScreenshot, setBrightness
from commands.dateTime import tellTime, tellMonth, tellDate, tellDay, tellYear 
from commands.package import updatePackages, installPackage, removePackage
from commands.health import calculateBMI
from commands.news import getNews
from commands.weather import getWeather
from commands.jokes import tellJoke
