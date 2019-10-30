# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:09:44 2019

@author: CLIENTE
"""
import time
import numpy as np
from moresorensen import ms

def MétodoDeRegiãoDeConfiança(dado):
    x = dado[1]
    def f(p):
        return dado[0](p,0)
    def grad(p):
        return dado[0](p,1)
    def hess(p):
        return dado[0](p,2)
    
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