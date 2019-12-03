# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 19:25:15 2019
@author: CLIENTE
"""

from Método_de_Penalidade import MétododePenalidade as MDP
import numpy as np


#G = np.asarray([[0.01,0],[0,1]])
#d = np.asarray([0,0])
#A = np.asarray([[10,-1],[1,0],[-1,0],[1,0],[-1,0]])
#b = np.asarray([10,2,-50,-50,-50])
#x = np.asarray([3,10])
#E = []
#J = [0,1,2,3,4]


#G = np.asarray([[9,0,0],[0,1,0],[0,0,9]])
#d = np.asarray([0,0,0])
#A = np.asarray([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
#b = np.asarray([-10,-10,1,-10,-10,-1])
#x = np.asarray([1,1,1])
#E = []
#J = [0,1,2,3,4,5]


G = np.asarray([[1,0],[0,1]])
d = np.asarray([6,0])
A = np.asarray([[0,-1],[1,0],[0,1]])
b = np.asarray([0,-1,0])
x = np.asarray([0,0])
E = []
J = [0,1,2]


def ActiveSet(G,d,A,b,E,J,x):
    w = E.copy()
    notw = J.copy()
    Aw = np.asarray([A[i] for i in w])
    
    

    
    
    k = 0
    while k < 1000:
        #computa o p
        if len(Aw) == 0:
            p = -np.linalg.solve(G,G@x+d)    
        else:
            def f(p):
                return np.dot(p,G@p)/2 + np.dot(G@x + d,p)
            def gradf(p):
                return np.dot(G,p) + G@x + d
            def hessf(p):
                return G
            def rest(p):    
                return np.dot(Aw,p)
            def gradrest(p):
                return Aw
            def hessrest(p):
                aa = np.zeros((len(Aw[0]),len(Aw[0])))
                hessrest = []
                for i in Aw:
                    hessrest.append(aa)
                return hessrest
            
            p = MDP([f,gradf,hessf,rest,gradrest,hessrest,np.zeros(len(x))])
        if np.dot(p,p) < 10**(-4):
            #definir os multiplicadores de lagrange
            ychapeu = np.linalg.lstsq(Aw.T,G@x+d,rcond=-1)[0]

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

print(ActiveSet(G,d,A,b,E,J,x))
