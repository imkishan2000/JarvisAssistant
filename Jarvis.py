import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listinging....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognize...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")    

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query   


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            print("searching wikipedia")
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            # print(songs)  
            os.startfile(os.path.join(music_dir, songs[0]))  
        elif 'close music' in query:
            try:
                os.close(music_dir) 
            except Exception as e:
                print(e)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}") 
        elif 'open code' in query:
            codepath = ""
            os.startfile(codepath)       

        elif 'exit' in query:
            exit(0)            