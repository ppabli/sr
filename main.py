import speech_recognition as sr
from gtts import *
import pyglet
import os


r = sr.Recognizer()

with sr.Microphone() as source:

	print("Di algo")

	try:

		audio = r.listen(source)
		text = r.recognize_google(audio, language = 'es-ES')
		print("Has dicho:", text)
		file = gTTS(text = text, lang = 'en', slow = False)
		filename = './test.mp3'
		file.save(filename)
		os.system('afplay  ' + filename)
		os.remove(filename)

	except:

		print("Ha ocurrido un error")
