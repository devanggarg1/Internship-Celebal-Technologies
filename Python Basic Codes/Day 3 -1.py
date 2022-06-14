# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 17:39:06 2022

@author: devan
"""

l1=eval(input(''))
l2=eval(input(''))
l3=[]
l4=[]
for i in range(1,len(l1),2):
    l3.append(l1[i])
for i in range(0,len(l2),2):
    l4.append(l2[i])
print("Element at odd-index positions from list one")
print("")
print(l3)
print("Element at even-index positions from list two")
print("")
print(l4)
l3=l3+l4
print("")
print(l3)