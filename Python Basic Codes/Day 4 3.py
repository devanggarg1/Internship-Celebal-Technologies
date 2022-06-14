# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 16:35:44 2022

@author: devan
"""

def largest():
    l1=eval(input(''))
    l1=list(l1)
    l1.sort()
    l2=l1[::-1]
    return l2[0]
    

result=largest()
print(result)
    