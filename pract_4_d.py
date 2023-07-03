# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 12:43:10 2023

@author: Aditi
"""

import spacy
nlp = spacy.blank("en")

str = "I love to study Natrual Language processing in python"

doc = nlp(str)
words = [ word.text for word in doc]
print(words)