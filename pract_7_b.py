# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 23:33:47 2023

@author: Aditi
"""
def FA(s):
    if len(s)<3:
        return "rejected"
    if s[0] =="1":
        if s[1]=="0":
            if s[0]=="1":
                for i in range(3,len(s)):
                    if s[i]!="1":
                        return "rejected"
                return "accepted"
            return "rejected"
        return "rejected"
    return "rejected"
inputs = ['1','10101','101','1011','01010','100','10111101','1011111',' ']
for i in inputs:
    print(FA(i))    
