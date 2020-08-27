import pyttsx3
from gtts import gTTs
import os
engine = pyttsx3.init()
engine.say("Địt con mẹ mày")
engine.runAndWait()
import pyttsx3
engine = pyttsx3.init() # object creation

tts = gTTs(text = engine, lang='vi')
tts.save(test.mp3)
os.system("start test.mp3")