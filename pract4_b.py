# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 12:38:12 2023

@author: Aditi
"""

import nltk 
from nltk.tokenize import RegexpTokenizer
tk = RegexpTokenizer('\s+', gaps=True)
str = "I love to study Natrual Language processing in python"
tokkens = tk.tokenize(str)
print(tokkens)