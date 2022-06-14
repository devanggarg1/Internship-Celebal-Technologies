# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 09:29:29 2022

@author: devan
"""

def user(a,b):
    
    def addition():
        sum=a+b
        return sum
    final=addition()
    print(final+5)

    
    
a=int(input())
b=int(input())
result=user(a,b)

print(result,"")
