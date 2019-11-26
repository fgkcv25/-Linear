# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:12:15 2019

@author: 05873472955
"""

import numpy as np

x = np.asarray([10,3,5])
A = np.asarray([[1,3,6],[3,2,5],[6,5,7]])
b = np.asarray([3,9,-10])

def MétodoDoGradienteConjugadoLINEAR(A,x,b):
    r = np.dot(A,x) - b
    p = -r
    while np.dot(r,r) > 10**(-4):
        y = np.dot(A,p)
        a = -np.dot(r,p)/np.dot(p,y)
        x = x + a*p
        r = np.dot(A,x) - b
        B = np.dot(r,y)/np.dot(p,y)
        p = -r + B*p
    return x

print(MétodoDoGradienteConjugadoLINEAR(A,x,b))