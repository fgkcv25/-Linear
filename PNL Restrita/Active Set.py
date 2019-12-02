# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:25:07 2019

@author: 05873472955
"""

import numpy as np
from gradconj import GradProj

G = np.asarray([[0.01,0],[0,1]])/2
d = np.asarray([0,0])
A = np.asarray([[10,-1],[1,0],[-1,0],[0,1],[0,-1]])
b = np.asarray([10,2,-50,-50,-50])
x = np.asarray([3,10])
E = []
J = [0,1,2,3,4]

def ActiveSet(G,d,A,b,x,E,J):
    n = len(x)
    w = []
    Aw = []
    notw = []
    for i in range(len(b)):
        if np.dot(A[i],x) == b[i]:
            w.append(i)
            Aw.append(A[i])
        else:
            notw.append(i)
    if len(Aw) != 0:
        Aw = np.asarray(Aw)
        
    
    
    k = 0
    while k < 500:
        ge = np.dot(G,x) + d
        if len(Aw) == 0:
            p = np.linalg.solve(G,-ge)
        else:
            p = GradProj(G,ge,Aw,np.zeros(n),np.zeros(n))
            print(ge)
        
        if np.dot(p,p) < 10**(-4):
            ychapeu = np.linalg.lstsq(Aw.T,ge,rcond=-1)[0]
            
            minychapeu = 0
            for i in range(len(w)):
                if w[i] in J:
                    if ychapeu[i] < minychapeu:
                        minychapeu = ychapeu[i]
                        i0 = i
            
            if minychapeu == 0:
                break
            else:
                w.pop(i0)
                Aw = np.asarray([A[i] for i in w])
                notw.append(i0)
        
        else:
            a = 1
            for i in notw:
                if np.dot(A[i],p) < 0:
                    if (b[i] - np.dot(A[i],x))/np.dot(A[i],p) < a:
                        a = (b[i] - np.dot(A[i],x))/np.dot(A[i],p)
                        blocking = i
            
            x = x + a*p
            if a < 1:
                w.append(blocking)
                Aw = np.asarray([A[i] for i in w])
                notw.pop(blocking)
        
        k = k+1
        
        y = np.linalg.lstsq(A.T,ge,rcond=-1)[0]
    return [x,y]
            
            
            
            
print(ActiveSet(G,d,A,b,x,E,J))