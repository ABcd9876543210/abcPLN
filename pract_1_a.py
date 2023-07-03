# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:19:19 2023

@author: Aditi
"""
from playsound import playsound
from gtts import gTTS
mytext = "hello every one we are doing Natrual Language Processing."
language = "en"

myobj = gTTS (text= mytext, lang= language, slow = False)
myobj.save("myfile_nlp.mp3")
playsound('myfile_nlp.mp3')