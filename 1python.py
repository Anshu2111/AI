# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:22:22 2019

@author: DELL
"""

import math
print ("Enter the values of D: ")
A=input()
A=A.split(',')
B=[]
for x in A:
    B.append(int(x))
    
C=50
H=30
E=[]
for D in B:
    y=math.sqrt((2*C*D)/H)
    E.append(int(y))
print(E)