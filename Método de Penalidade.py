# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 13:55:51 2019

@author: 05873472955
"""

import numpy as np
#
#def f(x):
#    return (1-x[0])**2
#
#def gradf(x):
#    return np.asarray([-2*(1-x[0]),0])
#
#def rest(x):
#    c1 = 10*(x[1]-x[0]**2)
#    return np.asarray([c1])
#
#def gradrest(x):
#    gradc1 = [-20*x[0], 10]
#    return np.asarray([gradc1])

def f(x):
    return -1
def gradf(x):
    return [0,0]
def rest(x):
    return np.asarray([x[0]**2 + x[1]**2 -25, x[0]*x[1] - 9])
def gradrest(x):
    return np.asarray([[2*x[0],2*x[1]],[x[1],x[0]]])






u = 1
n = 2
m = 1
#x = np.asarray([-1.2,1])
x = np.asarray([2,1])
t = 1
y = -u*rest(x)


def L(x,y):
    gradsum = 0
    for i in range(m):
        gradsum = y[i]*gradrest(x)[i]
    return gradf(x) - gradsum

while np.dot(L(x,y),np.transpose(L(x,y))) > 10**(-4):
    def Q(x,u):
        return f(x) + (u/2)*np.dot(rest(x),rest(x))
    def Qu(x):
        return Q(x,u)
    def gradQ(x,u):
        ci = 0
        for i in range(m):
            ci = ci + rest(x)[i]*gradrest(x)[i]
        return gradf(x) + u*ci
    
    def gradQu(x):
        return gradQ(x,u)
    
    a = 1
    c1 = 0.9
    k = 0
    while np.dot(gradQu(x),gradQu(x)) > t:
        p = -gradQu(x)
        if Qu(x+a*p) <= Qu(x) + c1*a*np.dot(gradQu(x),p):
            x = x + a*p
            k = k+1
        else:
            a = 0.9*a
        if k >= 500:
            break
    y = -u*rest(x)
    u = u+1
    t = t/2
    print(L(x,y))
        
print(x)