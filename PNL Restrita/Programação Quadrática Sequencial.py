# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:41:19 2019

@author: CLIENTE
"""

#y^ = (AAt)-1 A gradf
import numpy as np

#def f(x):
#    return np.log(1+x[0]**2) - x[1]
#def gradf(x):
#    return np.asarray([2*x[0]/(1+x[0]**2),-1])
#
#def c(x):
#    c1 = (1+x[0]**2)**2 + x[1]**2 - 4
#    return np.asarray([c1])
#def gradc(x):
#    gradc1 = [2*(1+x[0]**2)*2*x[0], 2*x[1]]
#    return np.asarray([gradc1])
#
#n = 2
#x = np.zeros(n) + 1
#y = np.zeros(len(c(x)))



def f(x):
    return (1-x[0])**2
def gradf(x):
    return np.asarray([-2*(1-x[0]),0])
def c(x):
    c1 = 10*(x[1]-x[0]**2)
    return np.asarray([c1])
def gradc(x):
    gradc1 = [-20*x[0], 10]
    return np.asarray([gradc1])
n = 2
m = 1
x = np.asarray([-1.2,1])
y = np.zeros(len(c(x)))


#Problem 4
#def f(x):
#    return (1/3)*(x[0] + 1)**3 + x[1]
#def gradf(x):
#    return np.asarray([(x[0]+1)**2,1])
#def c(x):
    



from Método_de_Restrições_Ativas import ActiveSet

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
        (p,ychapeu) = ActiveSet(B,gradf0,A,-c0,np.zeros(n))
        u = max(abs(ychapeu)) + 1
        a = 1
        while phi(x + a*p,u) > phi(x,u) + ni*a*(np.dot(gradf0,p) - u*sum(abs(c0))):
            a = t*a
        By2 = gradL(x,y)
        x = x+a*p
        By1 = gradL(x,y)
        By = By1 - By2
        s = a*p
        if np.linalg.norm(p) > 10**(-4):
            B = B - np.outer(np.dot(B,s),np.dot(B,s))/np.dot(s,np.dot(B,s)) + np.outer(By,By)/np.dot(By,s)
#        ychapeu = -u*c(x)
        py = ychapeu - y
        y = y+a*py
        f0 = f(x)
        c0 = c(x)
        gradf0 = gradf(x)
        A = gradc(x)
    return [x,f0]


SQP(x,y,f,c,gradf,gradc,n)