# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:21:42 2019

@author: 05873472955
"""

import numpy as np
from sympy import symbols, diff, evalf
x_1,x_2,x_3,x_4,x_5,x_6 = symbols('x_1 x_2 x_3 x_4 x_5 x_6')
funções = [10*(x_2-x_1**2),1-x_1,90**(1/2)*(x_4-x_3**2),1-x_3,10**(1/2)*(x_2+x_4-2),10**(-1/2)*(x_2-x_4)]
def func(x):
    return [funções[i].subs([(x_1,x[0]),(x_2,x[1]),(x_3,x[2]),(x_4,x[3])]) for i in range(6)]
função = 0
for i in funções:
    função = função + i**2
def func2(x):
    return função.subs([(x_1,x[0]),(x_2,x[1]),(x_3,x[2]),(x_4,x[3])])
gradiente = [diff(função, x_1), diff(função, x_2), diff(função, x_3), diff(função, x_4)]
hessiana = [[diff(gradiente[i],x_1),diff(gradiente[i],x_2),diff(gradiente[i],x_3),diff(gradiente[i],x_4)] for i in range(4)]

def grad(x):
    return np.asarray([gradiente[i].subs([(x_1,x[0]),(x_2,x[1]),(x_3,x[2]),(x_4,x[3])]) for i in range(4)],dtype='float')

def hess(x):
    return np.asarray([[hessiana[i][j].subs([(x_1,x[0]),(x_2,x[1]),(x_3,x[2]),(x_4,x[3])]) for i in range(4)] for j in range(4)],dtype='float')


x = np.asarray([-3,-1,-3,-1])
p = grad(x)
h = hess(x)
c1 = 0.1
c2 = 0.9
a = 1
pk = -np.linalg.solve(h,p)

i = 0
while np.dot(grad(x),grad(x)) > 10**-8:
    if func2(x+a*pk) <= func2(x) + c1*a*np.dot(grad(x),pk):
        pk = -np.linalg.solve(hess(x),grad(x))
        x = x+a*pk
    else:
        a = 0.9*a
