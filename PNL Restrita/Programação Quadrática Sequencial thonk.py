# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:41:19 2019

@author: CLIENTE
"""

#y^ = (AAt)-1 A gradf
import numpy as np
from Método_de_Restrições_Ativas import ActiveSet

#def f(x):
#    return (x[0] - 2)**2 + x[1]**2
#def gradf(x):
#    return np.asarray([2*x[0] + 4, 2*x[1]])
#def c(x):
#    c1 = (1-x[0])**3 - x[1]
#    c2 = x[0]
#    c3 = x[1]
#    return np.asarray([c1,c2,c3])
#def gradc(x):
#    c1 = np.asarray([-3*(1-x[0])**2,-1])
#    c2 = np.asarray([1,0])
#    c3 = np.asarray([0,1])
#    return np.asarray([c1,c2,c3])
#E = []
#J = [0,1,2]
#x = np.asarray([1,0])
#y = np.zeros(len(c(x)))



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
x = np.zeros(2) + 1
y = np.zeros(len(c(x)))
E = [0]
J = []


#def f(x):
#    return (1-x[0])**2
#def gradf(x):
#    return np.asarray([-2*(1-x[0]),0])
#def c(x):
#    c1 = 10*(x[1]-x[0]**2)
#    return np.asarray([c1])
#def gradc(x):
#    gradc1 = [-20*x[0], 10]
#    return np.asarray([gradc1])
#x = np.asarray([-1.2,1])
#y = np.zeros(len(c(x)))
#E = [0]
#J = []



    





def SQP(x,y,f,c,gradf,gradc,E,J):
    ni = 0.3
    t = 0.9
    c0 = c(x)
    gradf0 = gradf(x)
    A = gradc(x)
    B = np.identity(len(x))
    
    u = 1
    def gradL(x,y):
        return gradf(x) - np.dot(y,gradc(x))
    def phi(x,u):
        return f(x) + (1/u)*sum(abs(c(x)))
    
    
    k = 0
    while np.dot(gradL(x,y),gradL(x,y)) > 10**(-4):
        
        (p,ychapeu) = ActiveSet(B,gradf0,A,-c0,E,J,np.zeros(len(x)))
        py = ychapeu-y
        print(ychapeu)
        if 1/u < max(abs(ychapeu)) + 0.5:
            u = 1/(max(abs(ychapeu)) + 1)
        
        a = 1
        while phi(x + a*p,u) > phi(x,u) + ni*a*(np.dot(gradf0,p) - (1/u)*sum(abs(c0))):
            a = t*a
        print(a)
        
        xold = x.copy()
        x = x+a*p
        
        c0 = c(x)
        gradf0 = gradf(x)
        A = gradc(x)
        y = y+a*py
        
        By = gradL(x,y) - gradL(xold,y)
        s = x - xold
        if np.dot(s,By) >= 0.2*np.dot(s,np.dot(B,s)):
            teta = 1
        else:
            teta = 0.8*np.dot(s,np.dot(B,s))/(np.dot(s,np.dot(B,s)) - np.dot(s,By))
        r = teta*By + (1-teta)*np.dot(B,s)
        if np.linalg.norm(s) > 10**(-4):
            B = B - np.outer(np.dot(B,s),np.dot(B,s))/np.dot(s,np.dot(B,s)) + np.outer(r,r)/np.dot(r,s)
        
        k = k+1
        if k >= 10:
            break
    return x


print(SQP(x,y,f,c,gradf,gradc,E,J))
