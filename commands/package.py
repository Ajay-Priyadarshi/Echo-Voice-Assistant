import subprocess
from commands.utils import say

# def installPackage(packageName):
#     subprocess.run(['sudo', 'apt', 'install', '-y', packageName])
#     say(f"Package {packageName} installed.")

# def updatePackages():
#     subprocess.run(['sudo', 'apt', 'update', '-y'])
#     subprocess.run(['sudo', 'apt', 'upgrade', '-y'])
#     say("System packages updated.")

# def removePackage(packageName):
#     subprocess.run(['sudo', 'apt', 'remove', '-y', packageName])
#     say(f"Package {packageName} removed.")

def installPackage(packageName):
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f"sudo apt install -y {packageName}"])
    say(f"Installing package {packageName}.")

def updatePackages():
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f"sudo apt update -y && sudo apt upgrade -y"])
    say("Updating System packages.")

def removePackage(packageName):
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f"sudo apt remove -y {packageName}"])
    say(f"Removing package {packageName}.")