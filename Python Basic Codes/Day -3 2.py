# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 17:47:04 2022

@author: devan
"""

l1=eval(input(''))
n=int(input())
chunk_list=[l1[i:i+n] for i in range(0,len(l1),n)]
print("")
print(l1)
print("")
for i in range(0,n,1):
    print("Chunk ",i+1)
    print(chunk_list[i])
    print(chunk_list[i][::-1])
    print("")