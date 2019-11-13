# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:29:13 2019

@author: 05873472955
"""

#y^ = (AAt)-1 A gradf
import numpy as np

def f(x):
    return np.log(1+x[0]**2) - x[1]
def gradf(x):
    return np.asarray([2*x[0]/(1+x[0]**2),-1])

def c(x):
    c1 = (1+x[0]**2)**2 + x[1]**2 - 4
    return np.asarray([c1])
def gradc(x):
    gradc1 = [2*(1+x[0]**2)*2*x[0], 2*x[1]]
    return np.asarray([gradc1])

n = 2
x = np.zeros(n) + 1
y = np.zeros(len(c(x)))


from Gradiente_Projetado import GradProj

def SQP(x,y,f,c,gradf,gradc,n):
    ni = 0.3
    t = 0.9
    c0 = c(x)
    f0 = f(x)
    gradf0 = gradf(x)
    A = gradc(x)
    B = np.identity(len(x))
    def gradL(x,y):
        return gradf(x) - np.dot(y,gradc(x))
    def phi(x,u):
        return f(x) + u*sum(abs(c(x)))
    
    while np.dot(gradL(x,y),gradL(x,y)) > 10**(-4):
        p = GradProj(B,gradf0,A.transpose(),-c0,np.zeros(n))
        u = max(abs(y)) + 1
        a = 1
        while phi(x + a*p,u) > phi(x,u) + ni*a*(np.dot(gradf0,p) - u*sum(abs(c0))):
            a = t*a
        By2 = gradL(x,y)
        x = x+a*p
        By1 = gradL(x,y)
        By = By1 - By2
        s = a*p
        B = B - np.outer(np.dot(B,s),np.dot(B,s))/np.dot(s,np.dot(B,s)) + np.outer(By,By)/np.dot(By,s)
        
        ychapeu = -u*c(x)
        py = ychapeu - y
        y = y+a*py
        f0 = f(x)
        c0 = c(x)
        gradf0 = gradf(x)
        A = gradc(x)
    return [x,f0]


SQP(x,y,f,c,gradf,gradc,n)
