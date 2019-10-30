# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:09:44 2019

@author: CLIENTE
"""

from sympy import symbols, diff, evalf
import numpy as np
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11 = symbols('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11')
var = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]

def minalpha(fu,X,p,gradiente,n):
    a = 1
    def f(a):
        return fu(X+a*p)
    def grad(a):
        return np.dot(gradiente(X+a*p),p)
#    def grad(a):
#        result = np.asarray([expr.subs([(var[i],X[i] + a*p[i]) for i in range(n)]) for expr in gradiente],dtype=float)
#        return result
    
    c1 = 0.4
    a2 = 1
    p2 = -grad(a)
    k = 0
    while np.dot(grad(a),grad(a)) > 10**(-5):
        if f(a+a2*p2) <= f(a)+c1*a2*np.dot(grad(a),p2):
            a = a+a2*p2
            p2 = -grad(a)
            k = k+1
        else:
            a2 = 0.9*a2
            k = k+1
        if k >= 500:
            break
    return a

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
    while np.dot(grad(x),grad(x)) > 10**(-5):
        a = minalpha(f,x,p,grad,n)
        x = x+a*p
        g = grad(x)
        ga = grad(x+a*p)
        B = np.dot(ga,ga)/np.dot(g,g)
        p = -ga + B*p

        k = k+1
        if k >= 50:
            break
    return [x, f(x),grad(x)]