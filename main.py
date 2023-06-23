import speech_recognition as sr
import os
import sys

def say(text):
    print(f"\n{text}\n")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="en-US")
            print(f"Question: {text}")
            return text
        except Exception as e:
            print(e)
            return "Some error occurred. Please try again."

if __name__ == "__main__":
    say("Hello, I am Jarvis. How can I help you?")
    while True:
        text = listen()
        if "what is your name" in text:
            say("My name is Jarvis")
        elif "what is my name" in text:
            say("Your name is Maruf Sarker")
        elif "goodbye" or "close" in text:
            say("Goodbye")
            break
        
