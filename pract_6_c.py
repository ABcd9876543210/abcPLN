# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 13:29:45 2023

@author: Aditi
"""

import nltk
nltk.download('treebank')
from nltk.corpus import treebank_chunk
treebank_chunk.tagged_sents()[0]
treebank_chunk.chunked_sents()[0]
treebank_chunk.chunked_sents()[0].draw()