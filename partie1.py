# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 08:35:52 2022

@author: O-OUK
"""

def f(x,a,b):
    s=''
    for i in x[a:b]:
        s+=i
    l=len(s)
    return s,l

def s(x,y):
    return x+y
s(1,2.1)
s(False,2)

type(s(1,2.1))

def ch_fr(x):
    d={}
    d={i:x.count(i) for i in x}
    return d
ch_fr('test')


def re(x,y):
    
    for i in range(len(x)):
        print(x[i],y[len(x)-1-i],end='\n')
    return
re([1,2,3,5],[1,2,3,5])
        

import numpy as np

a = np.ones((1, 10)).reshape(2, -1)
b = np.zeros((1, 10)).reshape(2, -1)

def ar(a,b):
    s=[]
    s+=[[i for i in a[0]]+[i for i in b[0]]]
    s+=[[i for i in a[1]]+[i for i in b[1]]]
            
    
    return s


