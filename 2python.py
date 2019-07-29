# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:41:32 2019

@author: DELL
"""

print("Enter the no. of rows & columns: ")
A=input()
A=A.split(",")
B=[]

for i in A:
    B.append(int(i))
    
row=B[0]
column=B[1]
A=[[0 for i in range (int(column))] 
    for j in range (int(row))]

for j in range (int(column)):
    for i in range (int(row)):
        A[i][j]=(i*j)
        
print(A)