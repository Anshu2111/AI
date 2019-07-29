# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 15:03:28 2019

@author: DELL
"""

class Anshu:
    def a(self):
        import math
print("Enter the values of A")
B=input()
B=B.split(",")
C=[]

for x in B :
    B.append(int(x))
    
C=40
H=20
lt=[]

for y in C:
    z=math.sqrt((2*C*d)/H)
    lt.append(int(y))
print(lt)

def b(self):
    print("Enter the rows & columns: ")
l1=input()
l1=l1.split(",")
l2=[]
for i in l1:
    l2.append(int(i))
    
row=l2[0]
cloumn=l2[1]
l1=[[0 for i in range (int(column))] for j in range (int(row))]

for j in range (int(column)):
    for i in range (int(row)):
        l1[i][j]= (i*j)
        
print(l1)


def c(self):
    print ("Enter the words: ")
l1=input()
l1=l1.split(",")
l1.sort()
print(l1)

def e(self):
    print("Enter the sentence: ")
    m=input()
    n=m.split(",")
    p=[]
    
for i in n:
    if i not in p:
        p.append(i)

k=len(p)
for i in range(0,p):
    print(p[i], ":" ,n.coiunt(p[i]))

