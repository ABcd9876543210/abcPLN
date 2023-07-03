# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:35:38 2023

@author: Aditi
"""

import nltk
from nltk.tag import DefaultTagger
exptager = DefaultTagger('NN')
from nltk.corpus import treebank
testsentence = treebank.tagged_sents()[1000:]
print(exptager.evaluate(testsentence))

from nltk.tag import DefaultTagger
exptager = DefaultTagger('NN')
print(exptager.tag_sents([['Hi',''],['How','are','you','?']]))
