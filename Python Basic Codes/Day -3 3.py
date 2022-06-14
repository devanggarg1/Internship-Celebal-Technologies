# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 18:24:09 2022

@author: devan
"""

def CountFrequency(my_list):
 
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
 
    for key, value in freq.items():
        print ("% d : % d"%(key, value))
 
# Driver function
if __name__ == "__main__":
    my_list =eval(input(''))
 
    CountFrequency(my_list)