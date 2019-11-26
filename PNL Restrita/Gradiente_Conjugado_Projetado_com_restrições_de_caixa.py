# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:26:55 2019

@author: CLIENTE
"""

import numpy as np
from Gradiente_Conjugado_Projetado_com_restrições_de_igualdade import GradProj as GCP


#G = np.asarray([[0.01,0],[0,1]])
#d = np.asarray([0,0])
#x = np.asarray([3,10])
#l = np.asarray([2,-50])
#u = np.asarray([-50,50])


G = np.asarray([[9,0,0],[0,1,0],[0,0,9]])
d = np.asarray([0,0,0])
x = np.asarray([1,1,1])
l = np.asarray([-10,1,-10])
u = np.asarray([10,10,1])







def CP(x,l,u):
    val = np.zeros(len(x))
    li = []
    ui = []
    iT = []
    for i in range(len(x)):
        if x[i] <= l[i]:
            val[i] = l[i]
            li.append(i)
            iT.append(i)
        elif x[i] >= u[i]:
            val[i] = u[i]
            ui.append(i)
            iT.append(i)
        else:
            val[i] = x[i]
    return [val,li,ui,iT]

def g(x):
    return G@x+d

def tbarra(i):
    if g(x)[i] < 0:
        return (x[i]-u[i])/g[i]
    if g(x)[i] > 0:
        return (x[i] - l[i])/g[i]
    



def GradProjCaixa(G,d,l,u,x):
    def CPlu(x):
        return CP(x,l,u)
    
    k = 0
    while k < 200:
        
#        if KKT:
#            break
        
        xc = CPlu(x - (G@x+d))[0]
        
        A = []
        for i in CPlu(xc)[3]:
            Aa = [0 for i in range(len(x))]
            Aa[i] = x[i]
            A.append(Aa)
        A = np.asarray(A)
        b = []
        for i in CPlu(xc)[3]:
            if i in CPlu(xc)[1]:
                b.append(l[i])
            if i in CPlu(xc)[2]:
                b.append(u[i])
        x = GCP(G,d,A,b,xc)
        
        k = k+1
        print(x)
    return x 
    
    
    
print(GradProjCaixa(G,d,l,u,x))    
    
    
    
    
    
    
    
    
    
    
    
    
    
    