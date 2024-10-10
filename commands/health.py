from commands.utils import say, takeCommand

def calculateBMI():
    say("WHat is your height in meters?")
    height = takeCommand()
    say("What is your weight in Kilograms?")
    weight = takeCommand()
    try:
        bmi = float(weight)/(float(height)**2)
        bmi = round(bmi, 2)
        say(f"Your bmi is {bmi}.")
    except ValueError:
        say("height or weight not provided properly.")