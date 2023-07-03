# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 13:20:56 2023

@author: Aditi
"""

import spacy
nlp = spacy.load("en_core_web_sm")

text = ("when seabastian Thrun started working on self-driving cars at"
"Google in 2007, few people oustside of the company took him"
"Seroiusly,I can tell you very senior CEO's of major Amercan"
"car companies would shake my hand and turn away beacause I wasn't"
"worth talking to,said Thurn , in an interview with recorder earlier")
doc = nlp(text)
print("nouns:\n",[chunk.text for chunk in doc.noun_chunks])
print("verbs",[token.lemma_ for token in doc if token.pos_ =="VERB"])