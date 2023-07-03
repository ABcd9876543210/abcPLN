# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 23:47:35 2023

@author: Aditi
"""

import nltk
from nltk.corpus import wordnet
print(wordnet.synsets("computer"))

print(wordnet.synset("computer.n.01").definition())
print("Examples:", wordnet.synset("computer.n.01").examples())

print(wordnet.lemma('buy.v.01.buy').antonyms())