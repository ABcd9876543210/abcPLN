# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 12:08:33 2023

@author: Aditi
"""

import nltk
from nltk.corpus import wordnet
print(wordnet.synsets("computer"))

print(wordnet.synset("computer.n.01").definition())

print("Examples",wordnet.synset("computer.n.01").examples())

print(wordnet.synset("buy.v.01.buy").antonyms())
