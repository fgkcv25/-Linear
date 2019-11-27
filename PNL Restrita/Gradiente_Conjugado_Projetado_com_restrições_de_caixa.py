# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:26:55 2019
@author: CLIENTE
"""

import numpy as np
from Gradiente_Conjugado_Projetado_com_restrições_de_igualdade import GradProj as GCP


G = np.asarray([[0.01,0],[0,1]])
d = np.asarray([0,0])
x = np.asarray([3,10])
l = np.asarray([2,-50])
u = np.asarray([-50,50])


#G = np.asarray([[9,0,0],[0,1,0],[0,0,9]])
#d = np.asarray([0,0,0])
#x = np.asarray([1,1,1])
#l = np.asarray([-10,1,-10])
#u = np.asarray([10,10,1])







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


    



def GradProjCaixa(G,d,l,u,x):
    def CPlu(x):
        return CP(x,l,u)
    
    def g(x):
        return G@x+d
    
    def tlist(x):
        te = []
        for i in range(len(x)):
            if g(x)[i] < 0:
                te.append((x[i]-u[i])/g(x)[i])
            if g(x)[i] > 0:
                te.append((x[i]-l[i])/g(x)[i])
            else:
                te.append(float("inf"))
        t = list(set(te))
        return t

    
    def p(x,j):
        pe = []
        for i in range(len(x)):
            if g(x)[i] < 0:
               if t[j] < x[i]-u[i]/g(x)[i]:
                   pe.append(-g[i])
               else:
                   pe.append(0)
            elif g(x)[i] > 0:
                if t[j] < x[i]-l[i]/g(x)[i]:
                    pe.append(-g(x)[i])
                else:
                    pe.append(0)
            else:
                pe.append(g(x)[i])
        if j == len(tlist(x)) + 1:
            return -g(x)
        else:
            return np.asarray(pe)
    
    def flinha(x,j):
        return np.dot(d,p(x,j)) + np.dot(CPlu(x-t[j]*g(x))[0],np.dot(G,p(x,j)))

    def fduaslinhas(x,j):
        return np.dot(p(x,j),np.dot(G,p(x,j)))
                      
    def deltat(x,j):
        return -flinha(x,j)/fduaslinhas(x,j)
                
    
    
    
    
    
    
    
    
    
    k = 0
    while k < 200:
        
#        if KKT:
#            break
        
        t = tlist(x)
        tmin = 0
        for j in range(len(t)):
            deltatj = deltat(x,j)
            if deltatj >= 0 and deltatj < t[j+1] - t[j]:
                tmin = t[j] + deltatj

        xc = CPlu(x - tmin*g(x))[0]
        
        
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