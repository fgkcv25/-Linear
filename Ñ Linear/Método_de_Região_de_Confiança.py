# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:09:44 2019

@author: CLIENTE
"""

from sympy import symbols, diff, evalf
import numpy as np
from moresorensen import ms
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11 = symbols('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11')
var = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]
import time

def MétodoDeRegiãoDeConfiança(dado):
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
    delta = 1
    mi1 = 0.01
    mi2 = 0.9
    lambda1 = 1/2 
    lambda2 = 1/2
    k = 0

    while np.dot(grad(x),grad(x)) > 10**(-5):
        s = ms(grad(x),hess(x),delta)
        p = (-1)*(f(x) - f(x+s))/(np.dot(s,grad(x))+(1/2)*(np.dot(s,np.dot(hess(x),s))))
        if p >= mi1:
            x = x+s
        if p >= mi2:
            delta = delta/lambda1
        elif p >= mi1:
            delta = delta
        else:
            delta = lambda1*delta
        if k >= 50:
            break
    return [x, f(x),grad(x)]