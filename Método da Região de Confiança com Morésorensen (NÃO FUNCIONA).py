# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:36:36 2019

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
    return np.asarray([expr.subs([(a, x[0]), (y, x[1])]) for expr in gradiente_rosenbrock],dtype=float)


e1 = 0.1
e2 = 0.9
g1 = 0.1
g2 = 0.9

from scipy.linalg import norm, cholesky, solve
import numpy as np

def ms(g,H,delta):
    """
    Método de Moré e Sorensen para a solução do subproblema de região de confiança na norma 2.
    """
    theta = 0.0001
    eps_D = 0.1
    n = g.shape[0]
    value = 0
    gnorm = norm(g)
    g2D = gnorm/delta
    Hnorminf = norm(H,np.inf)
    HnormF = norm(H,'fro')
    lower = np.maximum(0, g2D - np.minimum(Hnorminf,HnormF))
    upper = np.maximum(0, g2D + np.minimum(Hnorminf,HnormF))
    Dlower = (1-eps_D)*delta
    Dupper = (1+eps_D)*delta
    
    if lower < 1.0e-12:
        lbd = 0.0
    else:
        lbd = np.maximum(np.sqrt(lower*upper),lower+theta*(upper-lower))

    identity = np.eye(n)
    i = 0
    while i < 101:
        new_lbd = -1
        Hlambda = H+lbd*identity
        try:
            # Cholesky returns a lower triangular factor L such that Hlambda = L*L.T
            R = cholesky(Hlambda)
            isPosDef = True
        except:
            isPosDef = False

        if isPosDef:
            s = - solve(R, solve(R.T,g))
            norms = norm(s)
            if ((lbd < 1.0e-12 and norms <= Dupper) or (norms >= Dlower and norms<= Dupper)):
                # Then we are finished. s is the solution.
                updates = i
                i = 101
                if (norms >= Dlower and norms<= Dupper):
                    text = "(Solution found in the boundary of the trust region.)"
                else:
                    text = "(Solution found in the interior of the trust region.)"

            w = solve(R.T,s)
            normw2 = norm(w)**2
            new_lbd = lbd + ((norms-delta)/delta)*(norms**2/normw2)
            if norms > Dupper:
                lower = lbd
            else:
                upper = lbd
            
            theta_range = theta * ( upper - lower )
            if new_lbd > lower + theta_range and new_lbd < upper - theta_range:
                lbd = new_lbd
            else:
                lbd = np.maximum(np.sqrt(lower*upper),lower+theta_range)
        else:
            lower = lbd
            lbd = np.maximum(np.sqrt(lower*upper),lower+theta*(upper-lower))

        i = i + 1
            
    if i == 100:
        print("Error: 100 iterations in MS.")

    return s

x = np.asarray([10,10.1])
delta = 1
H = np.asarray([[1,0],[0,1]])
s = ms(grad(x),H,delta)

while np.dot(grad(x),grad(x)) > 10**(-8):
    print(grad(x))
    s = ms(grad(x),H,delta)
    p = (-1)*(f(x) - f(x+s))/(np.dot(s,grad(x))+(1/2)*(np.dot(s,np.dot(H,s))))
    if p >= e1:
        x = x+s
    if p >= e2:
        delta = 2*delta
    elif p >= e1:
        delta = delta
    else:
        delta = delta/2