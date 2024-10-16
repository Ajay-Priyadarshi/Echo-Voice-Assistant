import subprocess
from commands.utils import say

def installPackage(packageName):
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f"sudo apt install -y {packageName}"])
    say(f"Installing package {packageName}.")

def updatePackages():
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f"sudo apt update -y && sudo apt upgrade -y"])
    say("Updating System packages.")

def removePackage(packageName):
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f"sudo apt remove -y {packageName}"])
    say(f"Removing package {packageName}.")