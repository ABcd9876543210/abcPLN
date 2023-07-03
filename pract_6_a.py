# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 13:07:44 2023

@author: Aditi
"""

import nltk 
from nltk import tokenize
nltk.download('punkt')
from nltk import tag
from nltk import chunk
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
para = "Hello! My name is Beena Kapdia. Today you'll be learning NTK."

sents = tokenize.sent_tokenize(para)
print('\n sensentense to tokenize\n ============\n', sents )

print('\n word to tokenize\n ============\n', sents )

for index in range(len(sents)):
    words = tokenize.word_tokenize(sents[index])
    print(words)
    
tagged_words =[]
for index in range(len(sents)):
    tagged_words.append(tag.pos_tag(words))
print("\n POS Tagging \n =========\n",tagged_words)
    
tree =[]
for index in range(len(sents)):
    tree.append(chunk.ne_chunk(tagged_words[index]))
print('\n chunking\n==========\n')
print(tree)    