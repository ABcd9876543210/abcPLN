# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 08:49:24 2023

@author: Aditi
"""

from nltk.tokenize import MWETokenizer
from nltk import sent_tokenize, word_tokenize
s  = "A typical wiki contains multiple pages for the subjects or scope of the project, and could be either open to the public or limited to use within an organization for maintaining its internal knowledge base."
mwe = MWETokenizer([('New','York'),('Hong','Kong')],separator='_')
for sent in sent_tokenize(s):
    print(mwe.tokenize(word_tokenize(sent)))