import speech_recognition
import pyttsx3
import time

engine = pyttsx3.init()
engine.say("Hello, could you write your name please")
engine.runAndWait()
name = input("what is your name: ")
engine.say(f"Hello {name}" + 'What u want me to say I am listen')
engine.runAndWait()
point = '.'
for i in range(5):
    point += "."
    print(point)
    time.sleep(1)
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("something")
    audio = recognizer.listen(source)
print("you said")
v=recognizer.recognize_google(audio)
print(v)
words= v
if "hello" in words:
     print(f"hello to u too!{name}")
elif "how are u" in words:
     print("I am well, thanks")
elif "goodbye" in words:
     print("goodbye to u too")
else:
     print("sorry i didn't understand")
