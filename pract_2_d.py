# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:12:47 2023

@author: Aditi
"""

import nltk
from nltk import tokenize
nltk.download('punkt')
nltk.download('words')
para = "Hello! My name is Abhishek Madhukar Gawade. Today you'll be learning NLTK under guidence prajakta mam."
sents = tokenize.sent_tokenize(para)
print("\n sentence tokenization\n ===================\n", sents)
print("\n words tokenization \n =====================\n")
for index in range(len(sents)):
    words = tokenize.word_tokenize(sents[index])
    print(words)
    
print('\n\n\n')