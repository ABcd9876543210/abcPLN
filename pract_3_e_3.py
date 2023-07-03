# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:52:18 2023

@author: Aditi
"""

import spacy 
import nltk
from nltk.tokenize import word_tokenize
sp = spacy.load('en_core_web_sm')

all_stopwords = sp.Defaults.stop_words
all_stopwords.add('play')

text = "Yashesh like to play football, however he is not too fond of tennis."
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]

print(tokens_without_sw)

all_stopwords.remove('not')
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]

print(tokens_without_sw)