# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.    
"""                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

import numpy as np

from sympy import symbols, diff, evalf
x,y = symbols('x y')
expr = (1-x)**2+10*(y-x**2)**2
gradiente_rosenbrock = [diff(expr, x), diff(expr, y)]



p = np.asarray([100,100])
a = p[0]
b = p[1]
grad = [expr.subs([(x, a), (y, b)]) for expr in gradiente_rosenbrock]
k = 0

while (grad[0]**2+grad[1]**2)**(0.5) > 10**(-8):
    p = p - [i for i in grad]
    a = p[0]
    b = p[1]
    grad = [expr.subs([(x, a), (y, b)]) for expr in gradiente_rosenbrock]
    print((grad[0]**2+grad[1]**2)**(0.5))
    k = k+1
    if k > 8000:
        break
    
print(k)
print(p)
