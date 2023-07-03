# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 22:50:07 2023

@author: Aditi
"""

from nltk.corpus import brown
from nltk.tag import RegexpTagger
test_sent = brown.sents(categories='news')[0]
regexp_tagger = RegexpTagger(
    [(r'^-?[0-9]+(.[0-9]+)?$','CD'),
     (r'(The|the|A|a|An|an)$','AT'),
     (r'.*able$','JJ'),
     (r'.*ness$','NN'),
     (r'.*ly$','RB'),
     (r'.*s$','NNS'),
     (r'.*ing$','VBG'),
     (r'.*ed$','VBD'),
     (r'.*','NN')
     ])
print(regexp_tagger)
print(regexp_tagger.tag(test_sent))