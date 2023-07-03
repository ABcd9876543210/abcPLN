# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:32:28 2023

@author: Aditi
"""

import speech_recognition as sr

r = sr.Recognizer()

#file = sr.AudioFile('audiofile.wav')

with sr.AudioFile('Ed-Sheeran-Shape-Of-You-Lyrics.wav') as source:
    audio_text = r.listen(source)
    text = r.recognize_google(audio_text, language="en",)

print(text)