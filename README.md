# Echo - Your Linux Python Voice Assistant 
![Echo - Your Linux Python Voice Assistant](images/Echo.png) 

Echo is a Python-based voice assistant tailored specifically for Linux environments, designed to help you manage your daily tasks effortlessly. Whether you need to open applications, check the weather, listen to music, or set reminders, Echo is here to assist you with voice commands.

## Features

- **Open Websites and Applications**: Launch your favorite websites and Linux applications with simple voice commands.
- **Music/Video Playback**: Play your preferred songs and videos.
- **Date and Time**: Get the current time, date, day, month, and year.
- **Health Management**: Calculate your BMI quickly.
- **News Updates**: Stay informed with the latest news headlines.
- **Weather Information**: Get real-time weather updates for any city.
- **System Operations**: Update your system, change volume levels, and set reminders.
- **Package Operations**: Add, update, or remove packages. 
- **Jokes**: Enjoy a good laugh with random jokes.
- **Reminders**: Set reminders to keep track of your important tasks.
- **Voice Interaction**: Interact with Echo using natural language commands.
- **Customizable Voices**: Switch between four available voices – Jack, Jessy, John, and Julie – using voice commands.
- **Wake Word Activation**: Use a wake word like "Wake up Echo" to activate the assistant, minimizing unnecessary processing when idle.


## Installation

### Prerequisites

- **Linux Distribution**: This application is optimized for Linux Mint Victoria 21.1 but should work on other Linux distributions with minor adjustments.
- **Python 3.7 or higher**: Ensure you have Python installed. You can download it from [here](https://www.python.org/downloads/).
- **pip**: Python package installer.
- **scrot**: for taking screenshots.
- **eSpeak**: For voice feedback.

    ```bash
    sudo apt-get install espeak scrot 
    ```

- **Additional Dependencies**: Depending on your system, you might need to install `amixer` for volume control and other utilities.

### Clone the Repository

```bash
git clone https://github.com/Ajay-Priyadarshi/Echo-Voice-Assistant.git
cd echo-assistant
```

### Install Dependencies

It's recommended to use a virtual environment.
```bash
pip install -r requirements.txt
```

### API Keys
Echo requires API keys for certain functionalities. These keys are managed using a .env file for security and convenience.

- **Create a .env File**
In the root directory of the project, create a .env file:
```bash
touch .env
```
- **Add Your API Keys**
Open the .env file in your favorite text editor and add your API keys:
```bash
NEWS_API_KEY=your_news_api_key_here
OPENWEATHER_API_KEY=your_openweather_api_key_here
```
**News API Key**: Sign up at NewsAPI to obtain your API key.

**OpenWeather API Key**: Sign up at OpenWeather to obtain your API key.

## Data Configuration
Populate the data directory with your preferred websites, applications, and music paths.

- **Websites:** Edit data/websites.py to include website names and URLs.
- **Applications:** Edit data/applications.py to include application names and their executable paths.
- **Music:** Edit data/music.py to include song names and their file paths.

## Usage
Run the assistant using the following command:
```bash
python assistant.py
```
Once running, Echo will greet you and start listening for your commands. You can interact with Echo using voice commands such as:

#### Open a Website or Application:
- Open YouTube
- Open Firefox
  
#### Play Music:
- Play Levatiting

#### Get Time and Date:
- What is the time?
- Tell me the date.

#### Health:
- Calculate BMI

#### News and Weather:
- What's the news?
- What's the weather in New York?

#### System Commands:
- Update the system
- Increase volume
- Set brightness to 50%
- Set reminder for 18:30 to call John
- Take screenshot

#### Fun:
- Tell me a joke

### Switch Voice:
Switch to Jack, Jessy, John (default Jack)

#### Sleep and Wake Commands:
- Go to sleep
- Wake up Echo
Wake Word Activation
To reduce unnecessary processing when idle, Echo listens for a specific wake word. By default, you can activate Echo by saying "Wake up Echo". While asleep, Echo will not respond to any commands except the wake word.

## Acknowledgements

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- eSpeak
- [Plyer](https://plyer.readthedocs.io/en/latest/)
- [NewsAPI](https://newsapi.org/)
- [OpenWeather](https://openweathermap.org/)
- [JokeAPI](https://jokeapi.dev/)
