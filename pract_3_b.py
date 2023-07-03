# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 11:29:59 2023

@author: Aditi
"""

import nltk
from nltk.corpus import wordnet
print(wordnet.synsets("computer"))
print(wordnet.synset("computer.n.01").lemma_names())

for e in wordnet.synsets("computer"):
    print(f'{e} --> {e.lemma_names()}')
          
print(wordnet.synset("computer.n.01").lemmas())

print(wordnet.lemma('computer.n.01.computing_device').synset())

print(wordnet.lemma('computer.n.01.computing_device').name())

syn = wordnet.synset('computer.n.01')
print(syn.hyponyms)

print([lemma.name() for synset in syn.hyponyms() for lemma in synset.lemmas()])

vehicle = wordnet.synset('vehicle.n.01')
car = wordnet.synset('car.n.01')
print(car.lowest_common_hypernyms(vehicle))