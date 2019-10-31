# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 18:26:15 2019

@author: CLIENTE
"""

from sympy import symbols, diff, evalf
import numpy as np
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11 = symbols('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11')
var = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]

def MétodoQuasiNewtonBFGS(dado):
    x = dado[4]
    função = dado[0]
    gradiente = dado[1]
    hessiana = dado[2]
    n = dado[3]
    def f(X):
        return função.subs([(var[i],X[i]) for i in range(n)])
    def grad(X):
        return np.asarray([expr.subs([(var[i],X[i]) for i in range(n)]) for expr in gradiente],dtype=float)
    def hess(X):
        return np.asarray([[expr.subs([(var[i],X[i]) for i in range(n)]) for expr in hessiana[j]] for j in range(n)],dtype=float)    
    c1 = 0.4
    a = 1
    p = -np.linalg.solve(hess(x),grad(x))
    k = 0
    B = np.identity(len(x))
    while np.dot(grad(x),grad(x)) > 10**(-4):
        if np.dot(grad(x),p) < 1000000000:
            if f(x+a*p) <= f(x)+c1*a*np.dot(grad(x),p):
                s = x+a*p - x
                y = grad(x+a*p) - grad(x)
                x = x+a*p
                B = B - np.outer(np.dot(B,s),np.dot(B,s))/np.dot(s,np.dot(B,s)) + np.outer(y,y)/np.dot(y,s)
                p = -np.linalg.solve(B,grad(x))
                k = k+1
            else:
                a = 0.9*a
            if k >= 1000:
                break
        else:
            break
    return [x, f(x),grad(x)]