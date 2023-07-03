# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 15:37:05 2023

@author: Aditi
"""

from inltk.inltk import setup
setup('hi')
from inltk.inltk import tokenize
hindi_text ="""काबुल के एक स्कूल के नजदीक बम विस्फोट होने से लगभग 85 लोगों की मृत्यु हो गई और 150 से अधिक लोग घायल हो गए।"""

token_result = tokenize(hindi_text, "hi")
print(token_result)
