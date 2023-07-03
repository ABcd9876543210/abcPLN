# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 23:00:55 2023

@author: Aditi
"""

from nltk.tag import UnigramTagger
from nltk.corpus import treebank
train_sents = treebank.tagged_sents()[:10]

tagger = UnigramTagger(train_sents)
print(treebank.sents()[0])
print('\n', tagger.tag(treebank.sents()[0]))

tagger.tag(treebank.sents()[0])

tagger = UnigramTagger(model={'Pierre':'NN'})
print('\n',tagger.tag(treebank.sents()[0]))