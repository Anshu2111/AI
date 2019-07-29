# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:57:10 2019

@author: DELL
"""

print("Enter the Sentence Below: ")
A= input()
B=A.split(' ')
C=[]

for x in B:
    if x not in C:
        C.append(x)

D=len(C)

for x in range(0,D):
    print(C[x], ":" , B.count(C[x]))