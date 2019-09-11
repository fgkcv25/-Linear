# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:59 2019

@author: 05873472955
"""

import numpy as np

def f(x,A):
    return np.dot(np.transpose(np.dot(A,x)),x)*(1/2) - np.dot(np.transpose(x),np.dot(A,np.ones((10000,1))))

def grad(x,A):
    return np.dot(A,x) - np.dot(A,np.ones((10000,1)))

n = 10000
A = np.random.rand(n,n)
A = np.transpose(A)*A/2
x = 2*np.ones((n,1))
p = -grad(x,A)
k = 0
downb = np.dot(np.transpose(grad(x,A)),grad(x,A))

while np.dot(np.transpose(p),p) > 10**(-3):
    a = -np.dot(np.transpose(p),grad(x,A))/np.dot(np.transpose(p),np.dot(A,p))
    x = x + a*p
    upb = np.dot(np.transpose(grad(x,A)),grad(x,A))
    b = upb/downb
    downb = upb
    p = -grad(x,A)+b*p
    k = k+1
    print(grad(x,A))
    print(k)
print(k)
