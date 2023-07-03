# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:19:56 2023

@author: Aditi
"""

import nltk
from collections import defaultdict
text = nltk.word_tokenize("Abhishek likes to play foot ball. Abhishek does not like to play cricket")
tagged = nltk.pos_tag(text)
print(tagged)

addNounWord =[]
count = 0

for words in tagged:
    val = tagged[count][1]
    if (val == 'NN' or val =='NNS' or val =='NNP'):
        addNounWord.append(tagged[count][0])
    count+=1
    
print(addNounWord)

temp = defaultdict(int)

for sub in addNounWord:
    for wrd in sub.split():
        temp[wrd]+=1
        
res = max(temp, key=temp.get)

print("word with maximum frequency:"+str(res))