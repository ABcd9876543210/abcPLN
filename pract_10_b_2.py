# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 09:29:28 2023

@author: Aditi
"""

import nltk
from nltk import PCFG

gramm = PCFG.fromstring('''
                          NP -> NNS[0.5]|JJ NNS[0.3]|NP CC NP[0.2]
                          NNS -> "men"[0.1]|"women"[0.2]|"children"[0.3]| NNS CC  NNS[0.4]
                          JJ -> "old"[0.4]|"yong"[0.6]
                          CC -> "and"[0.9] |"or"[0.1]

                         ''' )
                          
print(gramm)

viterbi_parser = nltk.ViterbiParser(gramm)
token = "old men and women".split()
obj = viterbi_parser.parse(token)
print("Outpu:t")
for x in obj:
    print(x)