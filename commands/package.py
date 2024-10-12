import subprocess
from commands.utils import say

def installPackage(packageName):
    subprocess.run(['sudo', 'apt', 'install', '-y', packageName])
    say(f"Package {packageName} installed.")

def updatePackages():
    subprocess.run(['sudo', 'apt', 'update', '-y'])
    subprocess.run(['sudo', 'apt', 'upgrade', '-y'])
    say("System packages updated.")

def removePackage(packageName):
    subprocess.run(['sudo', 'apt', 'remove', '-y', packageName])
    say(f"Package {packageName} removed.")
