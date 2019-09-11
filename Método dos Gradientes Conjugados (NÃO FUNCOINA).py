# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:59 2019

@author: 05873472955
"""

import numpy as np

from sympy import symbols, diff, evalf
a,y = symbols('a y')
expr = (1-a)**2+10*(y-a**2)**2
gradiente_rosenbrock = [diff(expr, a), diff(expr, y)]


def f(x):
    return expr.subs([(a, x[0]), (y, x[1])])

def grad(x):
    return np.asarray([[expr.subs([(a, x[0]), (y, x[1])])] for expr in gradiente_rosenbrock],dtype=float)





n = 2
x = 2*np.ones((n,1))
p = -grad(x)
c1 = 0.00005
c2 = 0.4
downb = np.dot(np.transpose(grad(x)),grad(x))
k = 1

while np.dot(np.transpose(p),p) > 10**(-3):
    if f(x+k*p) <= f(x)+c1*k*np.dot(np.transpose(grad(x)),p):
        if np.abs(np.dot(np.transpose(grad(x+k*p)),p)) <= -c2*np.dot(np.transpose(grad(x)),p):
            x = x + k*p
            upb = np.dot(np.transpose(grad(x)),grad(x))
            b = upb/downb
            downb = upb
            p = -grad(x)+b*p
            print(grad(x))
        else:
            k = 0.9*k
            print('aaa')
    else:
        k = 0.9*k
        print('bbb')
