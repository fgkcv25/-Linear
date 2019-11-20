# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:10:33 2019

@author: 05873472955
"""

from scipy.linalg import qr
import numpy as np

G = 2*np.asarray([[1,1,0],[1,2,1],[0,1,1]])
c = np.asarray([0,0,0])
A = np.matrix([1,2,3])
b = np.matrix([1])
x = np.asarray([-4,1,1])

def GradProj(G,c,A,b,x):
    QR0 = qr(A.T)[0]
    QR1 = qr(A.T)[1]
    for i in range(len(QR1)):
        if QR1[i].any() == 0:
            i0 = i-1
            break
        else:
            i0 = i
    Z = QR0[i0:-1]
    H = np.diag(np.diag(G))
    inv = np.linalg.inv(Z@H@Z.T)
    P = np.dot(Z.T,np.dot(inv,Z))
    
    def grad(x):
        return np.dot(G,x) + c

    r = grad(x)
    g = np.dot(P,r)
    d = np.copy(-g)
    
    while np.abs(np.dot(r,g)) > 10**(-4):
        a = np.dot(r,g)/np.dot(d,np.dot(G,d))
        x = x + a*d
        r_ = r + a*np.dot(G,d)
        g_ = np.dot(P,r_)
        b = np.dot(r_,g_)/np.dot(r,g)
        d = -g_ + b*d
        g = np.copy(g_)
        r = np.copy(r_)
    
    return x

#print(GradProj(G,c,A,b,x))