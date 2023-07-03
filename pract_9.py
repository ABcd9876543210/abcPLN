# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 13:55:30 2023

@author: Aditi
"""

import pandas as pd
import numpy as np

data = pd.read_csv("spam.csv", encoding='latin-1')

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

stemm = PorterStemmer()
corpus = []
for i in range(0, len(data)):
    s1 = re.sub('[a-zA-Z]',repl='', string=data['v2'][i])
    s1.lower()
    s1 = s1.split()
    s1 = [stemm.stem(word) for word in s1 if word not in set(stopwords.words('english'))]
    s1 = ''.join(s1)
    corpus.append(s1)
    
from sklearn.feature_extraction.text import CountVectorizer
Countvector = CountVectorizer()
x = Countvector.fit_transform(corpus).toarray()
print(x)
y = data['v1'].values
print(y)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, stratify=y, random_state=2)

from sklearn.naive_bayes import MultinomialNB
multmomial = MultinomialNB()
multmomial.fit(x_train, y_train)

y_pred = multmomial.predict(x_test)
print(y_pred)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(classification_report(y_test, y_pred))
print("accuracy_score:", accuracy_score(y_test, y_pred))