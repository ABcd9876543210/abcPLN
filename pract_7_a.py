# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 13:33:57 2023

@author: Aditi
"""

import nltk
from nltk import tokenize
grammar1 = nltk.CFG.fromstring("""
                               S ->VP
                               VP ->VP NP
                               NP ->Det NP
                               Det -> 'that'
                               NP -> singular Noun
                               NP -> 'flight'
                               VP -> 'Book'
                               """)
sentence = "Book that flight"
for index in range(len(sentence)):
    all_tokens = tokenize.word_tokenize(sentence)
print(all_tokens)

parser = nltk.ChartParser(grammar1)
for tree in parser.parse(all_tokens):
    print(tree)
    tree.draw()