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

Z = qr(np.transpose(A))[0][1:3].T
H = np.diag(np.diag(G))
inv = np.linalg.inv(Z.T@H@Z)
P = np.dot(Z,np.dot(inv,Z.T))

def grad(x):
    return np.dot(G,x) + c



#tem que ser viável
x = np.asarray([-4,1,1])
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

print(x)