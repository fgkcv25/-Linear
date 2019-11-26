# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:30:00 2019

@author: CLIENTE
"""

import numpy as np

def f(x):
    return (1-x[0])**2
def gradf(x):
    return np.asarray([-2*(1-x[0]),0])
def hessf(x):
    return np.asarray([[2*x[0],0],[0,0]])

def rest(x):
    c1 = 10*(x[1]-x[0]**2)
    return np.asarray([c1])
def gradrest(x):
    gradc1 = [-20*x[0], 10]
    return np.asarray([gradc1])
def hessrest(x):
    hessc1 = np.asarray([[-20,0],[0,0]])
    return np.asarray([hessc1])
x = np.asarray([-1.2,1])
func1 = [f,gradf,hessf,rest,gradrest,hessrest,x]


def f(x):
    return -1
def gradf(x):
    return np.asarray([0,0])
def hessf(x):
    return np.asarray([[0,0],[0,0]])
def rest(x):
    return np.asarray([x[0]**2 + x[1]**2 -25, x[0]*x[1] - 9])
def gradrest(x):
    return np.asarray([[2*x[0],2*x[1]],[x[1],x[0]]])
def hessrest(x):
    c1 = np.asarray([[2,0],[0,2]])
    c2 = np.asarray([[0,1],[1,0]])
    return np.asarray([c1,c2])
x = np.asarray([2,1])
func2 = [f,gradf,hessf,rest,gradrest,hessrest,x]


def f(x):
    return np.log(1+x[0]**2) - x[1]
def gradf(x):
    return np.asarray([2*x[0]/(1+x[0]**2),-1])
def hessf(x):
    return np.asarray([[-((2*x[0])**2)*(1/(1+x[0]**2)**2) + 2/(1+x[0]**2),0],[0,0]])

def rest(x):
    c1 = (1+x[0]**2)**2 + x[1]**2 - 4
    return np.asarray([c1])
def gradrest(x):
    gradc1 = [2*(1+x[0]**2)*2*x[0], 2*x[1]]
    return np.asarray([gradc1])
def hessrest(x):
    hessc1 = np.asarray([[4*(1+x[0]**2) + 4*x[0]*2*x[0],0],[0,2]])
    return np.asarray([hessc1])
x = np.asarray([2,2])
func3 = [f,gradf,hessf,rest,gradrest,hessrest,x]


def MétododePenalidade(dado):
    f = dado[0]
    gradf = dado[1]
    hessf = dado[2]
    rest = dado[3]
    gradrest = dado[4]
    hessrest = dado[5]
    x = dado[6]
    m = len(rest(x))
    
    u = 1
    t = 1
    y = -u*rest(x)
    
    def L(x,y):
        return gradf(x) - np.dot(y,gradrest(x))
    
    k = 0
    while np.dot(L(x,y),np.transpose(L(x,y))) > 10**(-5):
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
        def hessQ(x,u):
            ci = 0
            for i in range(m):
                ci = ci + np.outer(gradrest(x)[i],gradrest(x)[i]) + rest(x)[i]*hessrest(x)[i]
            return hessf(x) + u*ci
        def hessQu(x):
            return hessQ(x,u)
        
        
        a = 1
        j = 0
        while np.dot(gradQu(x),gradQu(x)) > t:
            p = -np.linalg.solve(hessQu(x),gradQu(x))
            x = x + a*p
            j = j+1
            if j > 400:
                break
                
        y = -u*rest(x)
        u = u+1
        t = t/2
        k = k+1
        if k > 400:
            break
    return x