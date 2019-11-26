# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 14:47:39 2019

@author: CLIENTE
"""

from Gradiente_Conjugado_Projetado_com_restrições_de_igualdade import GradProj as GCP
import numpy as np

#G = 2*np.asarray([[4,1,0],[1,2,1],[0,1,1]])
#c = np.asarray([0,4,6])
#A = np.asarray([[1,2,3],[0,0,1]])
#b = np.asarray([1,1])
#x = np.asarray([-4,1,1])
#E = [0]
#J = [1]

G = np.asarray([[0.01,0],[0,1]])
c = np.asarray([0,0])
A = np.asarray([[10,-1],[1,0],[-1,0],[1,0],[-1,0]])
b = np.asarray([10,2,-50,-50,-50])
x = np.asarray([3,10])
E = []
J = [0,1,2,3,4]


def ActiveSet(G,c,A,b,x,E,J):
    w = [E]
    notw = []
    for i in J:
        if np.dot(A[i],x) == b[i]:
            w.append(i)
        else:
            notw.append(i)
    n = len(x)
    k = 0
    Aw = np.asarray([A[i] for i in w])
    bw = np.asarray([b[i] for i in w])
    print(Aw)
    while 1 == 1:
        try:
            p = GCP(G,G@x+c,Aw,np.zeros(n),x)
        except:
            p = np.linalg.solve(G,-c)
        if np.dot(p,p) < 10**(-4):
            y = np.linalg.lstsq(Aw.T,G@x+c)[0]
            if min([y[i] for i in w]) >= 0:
                break
            else:
                minindex = 0
                for i in range(len(y)):
                    if y[i] < minindex:
                        minindex = y[i]
                        i0 = i
                if i0 in w:
                    w.pop(w.index(i0))
                    notw.append(i0)
                    Aw = np.asarray([A[i] for i in w])
                    bw = np.asarray([b[i] for i in w])
        else:
            listadoa = []
            for i in range(len(b)):
                if i in notw and np.dot(A[i],p) < 0:
                    listadoa.append((b[i] - np.dot(A[i],x))/np.dot(A[i],p))
            listadoa.append(1)
            a = min(listadoa)
            
            x = x+a*p
            
            for i in notw:
                if np.dot(A[i],x) == b[i]:
                    w = w.append(i)
                    notw.pop(i)
                    Aw = np.asarray([A[i] for i in w])
                    bw = np.asarray([b[i] for i in w])
                    break
        k = k+1
        print(A@x)
        if k > 100:
            break
    return [x,y]

print(ActiveSet(G,c,A,b,x,E,J))