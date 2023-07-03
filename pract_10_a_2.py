# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 14:26:45 2023

@author: Aditi
"""
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("D:/abhishek/model college/sem4/NLP/b.txt")
sample_text = state_union.raw("D:/abhishek/model college/sem4/NLP/c.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokanized = custom_sent_tokenizer.tokenize(sample_text)

def proces():
    try:
        for i in tokanized[:2]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
            
    except Exception as e:
        print(str(e))
        
        
proces()