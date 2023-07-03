from nltk.corpus import wordnet
print(wordnet.synsets("active"))

print(wordnet.lemma('active.a.01.active').antonyms())
