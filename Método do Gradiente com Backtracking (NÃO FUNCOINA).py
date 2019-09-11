# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:48:51 2019

@author: 05873472955
"""
import numpy as np
from sympy import symbols, diff, evalf
x,y = symbols('x y')
função = (y-x**2)**2-x**2
gradiente = [diff(função, x), diff(função, y)]

a = 1
p = np.asarray([1,1])
c1 = 10**(-4)
c2 = 0.9
def f(p):
    return função.subs([(x, p[0]), (y, p[1])])

def grad(p):
    return np.asarray([expr.subs([(x, p[0]), (y, p[1])]) for expr in gradiente])

while np.dot(grad(p),grad(p)) > 10**(-4):
    if f(p+a*(-grad(p))) <= f(p) + c1*a*np.dot(grad(p),-grad(p)):
        if np.dot(grad(p+a*(-grad(p))),-grad(p)) >= c2*np.dot(grad(p),-grad(p)):
            p = p+a*(-grad(p))
        else:
            a = 0.9*a
            print(a)
            print('ese é o paso 2')
    else:
        a = 0.9*a
        print(a)