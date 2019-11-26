# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 19:25:15 2019

@author: CLIENTE
"""

from Gradiente_Conjugado_Projetado_com_restrições_de_igualdade import GradProj as GCP
import numpy as np


G = np.asarray([[0.01,0],[0,1]])
d = np.asarray([0,0])
A = np.asarray([[10,-1],[1,0],[-1,0],[1,0],[-1,0]])
b = np.asarray([10,2,-50,-50,-50])
x = np.asarray([3,10])
E = []
J = [0,1,2,3,4]



#problema minimizar a quadrática com G e d, s.a. Ax = b
#com E e J


def ActiveSet(G,d,A,b,E,J,x):
    w = E.copy()
    notw = J.copy()
    Aw = np.asarray([A[i] for i in w])
    bw = np.asarray([b[i] for i in w])
    
    
    
    
    
    k = 0
    while k < 10:
        print(Aw)
        
        #computa o p
        if len(Aw) == 0:
            p = np.linalg.solve(G,G@x+d)
        else:
            p = GCP(G,G@x+d,Aw,np.zeros(len(x)),np.zeros(len(x)))
        
        
        if np.dot(p,p) < 10**(-4):
                
            #definir os multiplicadores de lagrange
            try:
                ychapeu = np.linalg.lstsq(Aw.T,G@x+d)[0]
            except:
                ychapeu = [0 for i in w]
            minychapeu = 0
            for i in range(len(w)):
                if w[i] in J:
                    if ychapeu[i] < minychapeu:
                        minychapeu = ychapeu[i]
                        i0 = i
            
            #checa se é solução ou continua
            if minychapeu == 0:
                break
            else:
                notw.append(w[i0])
                w.pop(i0)
                Aw = np.asarray([A[i] for i in w])
                bw = np.asarray([b[i] for i in w])

        else:
            
            #computa o a
            listadoa = [1]
            for i in notw:
                if np.dot(A[i],p) < 0:
                    listadoa.append((b[i] - np.dot(A[i],x))/np.dot(A[i],p))
            a = min(listadoa)
            
            x = x+a*p
            
            for i in range(len(notw)):
                if np.dot(A[notw[i]],x) == b[i]:
                    w.append(notw[i])
                    notw.pop(i)
                    Aw = np.asarray([A[i] for i in w])
                    bw = np.asarray([b[i] for i in w])
                    break
        k = k+1
        print(k)
    return x
            
            

print(ActiveSet(G,d,A,b,E,J,x))
            
            
            

            
            
            
            
        
        
        
        