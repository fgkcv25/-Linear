# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 19:25:15 2019
@author: CLIENTE
"""

from Gradiente_Conjugado_Projetado_com_restrições_de_igualdade import GradProj as GCP
import numpy as np


#G = np.asarray([[0.01,0],[0,1]])
#d = np.asarray([0,0])
#A = np.asarray([[1,0],[-1,0],[0,1],[0,-1]])
#b = np.asarray([2,-50,-50,-50])
#x = np.asarray([3,10])
#E = []
#J = [0,1,2,3]


#G = np.asarray([[9,0,0],[0,1,0],[0,0,9]])
#d = np.asarray([0,4,2])
#A = np.asarray([[1,7,5],[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
#b = np.asarray([13,-10,-10,1,-10,-10,-1])
#x = np.asarray([1,1,1])
#E = [0]
#J = [1,2,3,4,5,6]


#G = np.asarray([[1,0],[0,1]])
#d = np.asarray([6,0])
#A = np.asarray([[0,-1],[1,0],[0,1]])
#b = np.asarray([0,-1,0])
#x = np.asarray([0,0])
#E = []
#J = [0,1,2]


#G = np.asarray([[1., 0.],
#       [0., 1.]])
#d = np.asarray([-551.,  550.])
#A = np.asarray([[ 3. ,  0.5],
#       [ 1. ,  6. ],
#       [-1. ,  0. ]])
#b = np.asarray([-0.5, -9.5, -0. ])
#x = np.linalg.lstsq(A,b,rcond=-1)[0]
#E = []
#J = [0,1,2]


#problema minimizar a quadrática com G e d, s.a. Ax >= ou = b
#com E e J sendo a lista dos índices em que é = e >=, respectivamente


def ActiveSet(G,d,A,b,E,J,x):
    w = []
    Aw = []
    notw = []
    for i in range(len(b)):
        if abs(np.dot(A[i],x) - b[i]) < 10**-3:
            print(np.dot(A[i],x))
            w.append(i)
            Aw.append(A[i])
        else:
            notw.append(i)
    if len(Aw) != 0:
        Aw = np.asarray(Aw)

    
    k = 0
    while k < 1000:
        #computa o p
        ge = np.dot(G,x) + d
        if len(Aw) == 0:
            p = np.linalg.solve(G,-ge)    
        else:
            p = GCP(G,ge,Aw,np.zeros(len(Aw)),np.zeros(len(x)))

            
        if np.dot(p,p) < 10**(-4):
            #definir os multiplicadores de lagrange
            try:
                ychapeu = np.linalg.lstsq(Aw.T,ge,rcond=-1)[0]
            except:
                pass

            minychapeu = 0
            for i in range(len(w)):
                if w[i] in J:
                    if ychapeu[i] < minychapeu:
                        minychapeu = ychapeu[i]
                        i0 = i
            #checa se é solução ou continua
            if minychapeu >= 0:
                break
            else:
                notw.append(w[i0])
                w.pop(i0)
                Aw = np.asarray([A[i] for i in w])
        
        else:
            a = 1
            for i in range(len(notw)):
                if np.dot(A[notw[i]],p) < 0:
                    if a > (b[notw[i]] - np.dot(A[notw[i]],x))/np.dot(A[notw[i]],p):
                        a = (b[notw[i]] - np.dot(A[notw[i]],x))/np.dot(A[notw[i]],p)
                        i0 = i
            x = x + a*p
            if a < 1:
                w.append(notw[i0])
                notw.pop(i0)
                Aw = np.asarray([A[i] for i in w])


        k = k+1
    y = np.linalg.lstsq(A.T,G@x+d,rcond=-1)[0]
    return [x,y]

#print(ActiveSet(G,d,A,b,E,J,x))