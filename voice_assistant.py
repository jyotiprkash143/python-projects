import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import time
import pyjokes
import os

#craeting a function for speech o text
def speech_to_text():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print('listing...you can speak now!!')
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("recognising.....")
            data=recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("sorry voice didnt recognise......")
#creating a function for text to speech 
def text_to_speech(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',130)
    engine.say(x)
    engine.runAndWait()
if __name__=="__main__":
   if speech_to_text().lower()=='hello rinku':
     while True:
        data='hello i am activated, how can i help you'
        text_to_speech(data)

        
        data1=speech_to_text().lower()
        if 'your name' in data1:
             x='my name is rinku'
             text_to_speech(x)
        elif 'your age' in data1:
             x='my age is 25'
             text_to_speech(x)
        elif 'time' in data1:
             time=datetime.datetime.now().strftime("%I%M%p")
             text_to_speech(time)
        elif 'youtube' in data1:
             webbrowser.open("https://www.youtube.com/")
        elif 'google' in data1:
             webbrowser.open("https://www.google.com/")
        elif 'joke' in data1:
             joke=pyjokes.get_joke(language='en',category='neutral')
             text_to_speech(joke)
        #here i am selecting song from my own file
        elif'play song' in data1:
             add=r"C:\Users\user\Desktop\song"
             listsong=os.listdir(add)
             
             os.startfile(os.path.join(add,listsong[0]))
        elif 'exit' in data1:
             data4='thank you bye bye'
             text_to_speech(data4)
             break
     else:         
        print('plz say "hello rinku"to start')
    
