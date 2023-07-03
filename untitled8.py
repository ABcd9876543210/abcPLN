# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 12:26:41 2023

@author: Aditi
"""

import nltk
from nltk.corpus import wordnet
print(wordnet.synset("computer"))

print(wordnet.synset("computer.n.01").lemma_names())

for e in wordnet.synset("computer"):
    print(f'{e}-->{e.lemma_names()}')
print(wordnet.synset('computer.n.01').lemma_names())
print(wordnet.lemma('computer.n.01.computing_device').synset())

