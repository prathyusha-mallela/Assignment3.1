# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 22:19:17 2017

@author: Prathyusha Mallela
"""

#Assignment 3.1.2
def myfilter(val_del,lst):
    final_list=list(set(lst)-set(val_del))
    return final_list
    
lst=[1,2,3,4,5]
t=myfilter([1,3,4],lst)
print(t)