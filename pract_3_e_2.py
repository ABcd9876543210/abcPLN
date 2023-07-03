# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 11:46:45 2023

@author: Aditi
"""

import gensim
from gensim.parsing.preprocessing import remove_stopwords
from nltk.tokenize import word_tokenize
text = "Yashesh likes to play football, however he is not too fond of tennis."
filtered_sentense = remove_stopwords(text)

print(filtered_sentense)

all_stpwords = gensim.parsing.preprocessing.STOPWORDS
print( all_stpwords)

from gensim.parsing.preprocessing import STOPWORDS
all_stpwords_genism = STOPWORDS.union(set(['likes','play']))
text = "Yashesh likes to play football, however he is not too fond of tennis."
text_tokens = word_tokenize(text)

tokens_without_sw = [word for word in text_tokens if not word in all_stpwords]
                     
print(tokens_without_sw)

print("========================================")
all_stpwords_genism = STOPWORDS
sw_list = {"not"}
all_stpwords_genism = STOPWORDS.difference(sw_list)
text = "Yashesh likes to play football, however he is not too fond of tennis."
text_tokens = word_tokenize(text)

tokens_without_sw = [word for word in text_tokens if not word in all_stpwords_genism]
print(all_stpwords_genism)
print(tokens_without_sw)