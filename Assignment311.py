# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 22:21:41 2017

@author: Prathyusha Mallela
"""

#Assignment 3.1.1
def myreduce(func, iterable, start=None):
    it = iter(iterable)
    if start is None:
        try:
            start = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = start
    for x in it:
        accum_value = func(accum_value, x)
    return accum_value

myreduce((lambda x,y:x+y),[1,2,3,4])