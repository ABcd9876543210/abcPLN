# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 12:50:23 2023

@author: Aditi
"""

from gensim.utils import tokenize

str = "I love to study Natrual Language processing in python"
print(list(tokenize(str)))