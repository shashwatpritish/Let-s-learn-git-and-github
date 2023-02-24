import pyttsx3 as p
from time import sleep
audio = input("Enter what do you want to speak: ")
sleep(1)
print(audio)
p.speak(audio)