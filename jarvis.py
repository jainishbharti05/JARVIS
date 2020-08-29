import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init()
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <= 17:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir")
    speak("I am Jarvis, your personal assistant. Please tell me how can i be of your Help?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        r.energy_threshold = 800
        audio = r.listen(source)
        # print("Recognizing.....")
        # query = r.recognize_google(audio, language="en-in")
        # print(f"You said: {query}")
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language= "en-in")
        print(f"You said: {query}")
        # speak("You said"+ query)

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    # speak("Hello Sir ! Can i be of any help?")
    wishMe()
    while True:
        query = takeCommand().lower()
    # Logic to perform tasks based on queries
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query, sentences=2)
            print("According to wikipedia", results)
            speak("According to wikipedia....")
            speak(results)
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            speak("Playing music for you Sir")
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            # print(songs)
            # random_song = random.choices(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        elif 'time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {str_time}")
        elif 'quit' in query:
            speak("thankyou sir, Jarvis signing off here. Have a good day Sir")
            exit()
            
