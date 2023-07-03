# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 13:07:23 2023

@author: Aditi
"""

def FA(s):
    size = 0
    for i in s:
        if i =='a' or i =='b':
            size+=1
        else:
            return "rejected"
    if size>=3:
        if s[size-3] =='b':
            if s[size-2] =='b':
                if s[size-1] =='a':
                    return "accepted"
                return "rejected"
            return "rejected"
        return "rejected"
    return "rejected"
inputs = ['bba','ababba','abba','abb','baba','bbb']
for i in inputs:
    print(FA(i))