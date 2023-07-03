# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 23:08:36 2023

@author: Aditi
"""

from __future__ import with_statement
import re

words = []
testword = []
ans = []
print("MENU")
print('------------')
print("1. Hash tag segmentation")
print("2. URL segmentation")
print("enter input choice")

choice = int(input())

if choice == 1:
    text = "#whatismyname"
    print("input with Hash Tag",text)
    pattern = re.compile("[^\w']")
    a = pattern.sub(''.text)
elif choice ==2:
    text = "www.whatismyname.com"
    print("inupt with URL", text)
    a = re.split('\s|(?<!\d)[,.](?!\d)', text)
    splitwords = ["www","com","in"]
    a = "".join([each for each in a if each not in splitwords])
else:
    print("wrong choice....try again")
    
print(a)

for each in a:
    testword.append(each)    
test_lenth = len(testword)

with open('word.txt','r') as f :
    lines = f.readlines()
    words =[(e.strip()) for e in lines]             
def Seg(a, lenth):
    ans =[]
    for k in range(0, lenth+1):
        if a[0:k] in words:
            print(a[0:k],"-appears in the corpus")
            ans.append(a[0:k])
            break
        if ans != []:
            g = max(ans, key=len)
            return g
test_tot_itr =0
answer =[]
Score = 0

N  = 37
M = 0
C = 0

while test_tot_itr < test_lenth:
    ans_word = Seg(a, test_lenth)
    if ans_word != 0:
        test_itr = len(ans_word)
        answer.append(ans_word)
        a = a[test_itr:test_lenth]
        test_tot_itr += test_itr
        
Aft_Seg = "".join([each for each in answer])
print("output")
print("=======")
print(Aft_Seg)

C = len(answer)
Score  = C*N/N
print("Score", Score)