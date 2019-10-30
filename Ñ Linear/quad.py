# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 17:33:28 2019

@author: CLIENTE
"""

import numpy as np
from sympy import symbols, diff
x1,x2,x3,x4,x5,x6,x7,x8,x9 = symbols('x1 x2 x3 x4 x5 x6 x7 x8 x9')
var = [x1, x2, x3, x4, x5, x6, x7, x8, x9]

dados = []

def Quadrática(numero):
    n = 2
    m = 2
    f1 = x1
    f2 = x2
    função = f1**2 + f2**2
    
    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

quad = [Quadrática, [1,1]]