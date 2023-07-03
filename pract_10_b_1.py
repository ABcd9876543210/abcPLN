# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 09:01:07 2023

@author: Aditi
"""

import nltk
import nltk.parse.viterbi
import nltk.parse.pchart

def give(t):
    return t.label() =='VP' and len(t)>2 and t[1].label() =='NP' and (t[2].label() =='PP-DTV' or t[2].label()=='NP') and('give 'in t[0].leaves() or 'gave' in t[0].leaves())

def sent(t):
    return ''.join(token for token in t.leaves() if token[0] not in '*-0')

def print_node(t, width):
    op = "%s %s: %s/ %s: %s "%(sent(t[0]), t[1].label(), sent(t[1]), t[2].label(), sent(t[2]))
    
    if len(op)> width:
        op = op[:width] + "..."
    print(op)
    
for tree in nltk.corpus.treebank.parsed_sents():
    for t in tree.subtrees(give):
        print_node(t, 72)