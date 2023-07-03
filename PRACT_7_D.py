
import nltk
from nltk import tokenize
grammar = nltk.CFG.fromstring("""
                              S -> NP VP
                              PP -> P NP
                              NP -> Det N | Det N PP | 'I'
                              VP -> V NP | VP PP
                              Det -> 'a' | 'my'
                              N -> 'bird' | 'balcony'
                              V -> 'saw'
                              P -> 'in'
                              """)
sentence = "I saw a bird in my balcony"
for index in range(len(sentence)):
    all_tokens = tokenize.word_tokenize(sentence)
print(all_tokens)

parser = nltk.ChartParser(grammar)
for tree in parser.parse(all_tokens):
    print(tree)
    tree.draw()