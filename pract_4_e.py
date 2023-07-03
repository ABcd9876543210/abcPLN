# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 12:46:00 2023

@author: Aditi
"""

import keras
from keras.preprocessing.text import text_to_word_sequence
str = "I love to study Natrual Language processing in python"

tokens = text_to_word_sequence(str)
print(tokens)