# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:35:25 2019

@author: 05873472955
"""

from sympy import symbols, diff, evalf
import numpy as np
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11 = symbols('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11')
var = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]

def MétodoDeGradienteConjugado(dado):
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

    k = 0
    p = -grad(x)
    g = grad(x)
    a = 1
    c1 = 0.4
    while np.dot(grad(x),grad(x)) > 10**(-4):
        if f(x+a*p) <= f(x)+c1*a*np.dot(grad(x),p):
            g = grad(x)
            x = x+a*p
            ga = grad(x)
            B = np.dot(ga,ga)/np.dot(g,g)
            p = -ga + B*p
            a = 1
            k = k+1
            if k >= 50:
                break
        else:
            a = 0.9*a

    return [x, f(x),grad(x)]