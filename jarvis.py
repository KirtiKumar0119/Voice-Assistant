import pyttsx3
import datetime
import speech_recognition as sr


engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#speak("this is cheap jarvis AI assistant")
def time():
    Time= datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
#time()
def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
#date()
def wishme():
    speak("welcome back sir")
    speak("the current time is ")
    time()
    speak("the current date is " )
    date()
    hour= datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning your majesty")
    elif hour>=12 and hour<18:
        speak("Good afternoon your majesty")
    elif hour>=18  and hour<24:
        speak("Good evening your majesty")
    else:
        speak("its too dark. Good night sir")
#wishme()
def takeCommand():

    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening ...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("kindly repeat ")
        return "None"
    return query
takeCommand()
'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("Say something!")
      audio = r.listen(source)

# Speech recognition using Google Speech Recognition
    try:
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        print("Could not understand audio")
'''