# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 16:48:32 2023

@author: Aditi
"""

import nltk
from nltk.corpus import brown
print('file ids of brown n corpus\n', brown.fileids())

ca01 = brown.words('ca01')
print('\n ca01 has following word:\n', ca01)

print('\n ca01 has ', len(ca01),'words')

print('\n \n categories oe file in brown corpus:\n')
print(brown.categories())

print('\n \n Static for each text: \n')
print('AvgWordLen\t AvgSentenceLen\t no.ofTimesachWordAppearsOnAvg\t\t FileName')
for fileid in brown.fileids():
    num_chars = len(brown.raw(fileid))
    num_words = len(brown.words(fileid))
    num_sents = len(brown.sents(fileid))
    num_vocab = len(set([w.lower() for w in brown.words(fileid)]))
    print('\t\t',int(num_chars/num_words),'\t\t\t',int(num_words/num_sents),'\t\t\t', int(num_words/num_vocab),'\t\t\t\t\t\t',fileid)
    