# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 14:35:40 2019

@author: CLIENTE
"""

import numpy as np
#from sympy import symbols, diff, atan, exp, evalf, log, Abs, Derivative, sign, sin, cos
from sympy import *
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11 = symbols('x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11')
var = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]

dados = []

def Rosenbrock(numero):
    n = 2
    m = 2
    f1 = 10*(x2-x1**2)
    f2 = 1-x1
    função = f1**2 + f2**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func1 = (Rosenbrock, [-1.2,1])
dados.append(func1)



def Freudenstein_and_Roth(numero):
    n = 2
    m = 2
    f1 = -13 + x1 + ((5-x2)*x2-2)*x2
    f2 = -29 + x1 + ((x2+1)*x2-14)*x2
    função = f1**2 + f2**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func2 = (Freudenstein_and_Roth, [0.5,-2])
dados.append(func2)



def PowellBSF(numero):
    n = 2
    m = 2
    f1 = (10**4)*x1/x2
    f2 = exp(-x1) + exp(-x2) - 1.0001
    função = f1**2 + f2**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func3 = (PowellBSF, [0,1])
dados.append(func3)



def BrownBSF(numero):
    n = 2
    m = 3
    f1 = x1 - 10**6
    f2 = x2 - 2*10**(-6)
    f3 = x1*x2-2
    função = f1**2 + f2**2 + f3**2
    
    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func4 = (BrownBSF, [1,1])
dados.append(func4)



def Beale(numero):
    n = 2
    m = 3
    y = [1.5,2.25,2.625]
    fi = [y[i]-x1*(1-x2**(i+1)) for i in range(m)]
    função = 0
    for f in fi:
        função = função + f**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func5 = (Beale, [1,1])
dados.append(func5)



def Jennrich_and_Sampson(numero):
    n = 2
    m = 10
    fi = [2+2*i - (exp(i*x1)+exp(i*x2)) for i in [i+1 for i in range(m)]]
    função = 0
    for f in fi:
        função = função + f**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func6 = (Jennrich_and_Sampson, [0.3,0.4])
dados.append(func6)



def Helical_Valley(numero):
    n = 3
    m = 3
    def o(x1,x2,n):
        if n == 1:
            return atan(x2/x1)/(2*np.pi)
        if n == -1:
            return atan(x2/x1)/(2*np.pi) + 0.5
    f1_1 = 10*(x3-10*o(x1,x2,1))
    f1_2 = 10*(x3-10*o(x1,x2,-1))
    f2 = 10*((x1**2 + x2**2)**(1/2) - 1)
    f3 = x3
    fi = [f1_1,f2,f3]
    função1 = 0
    for f in fi:
        função1 = função1 + f**2
    fi = [f1_2,f2,f3]
    função2 = 0
    for f in fi:
        função2 = função2 + f**2

    if numero == 0:
        if X[0] > 0:
            return função1.subs([(var[i],X[i]) for i in range(n)])
        elif X[0] < 0:
            return função2.subs([(var[i],X[i]) for i in range(n)])
    elif numero == 1:
        if X[0] > 0:  
            grad = [diff(função1,xi) for xi in var[0:n]]
            return np.asarray([expr.subs([(var[i],X[i]) for i in range(n)]) for expr in grad],dtype=float)
        elif X[0] < 0:
            grad = [diff(função2,xi) for xi in var[0:n]]
            return np.asarray([expr.subs([(var[i],X[i]) for i in range(n)]) for expr in grad],dtype=float)

    elif numero == 3:
        if X[0] > 0:
            grad = [diff(função1,xi) for xi in var[0:n]]
            hess = [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
            return np.asarray([[expr.subs([(var[i],X[i]) for i in range(n)]) for expr in hess[j]] for j in range(n)],dtype=float)
        elif X[0] < 0:
            grad = [diff(função2,xi) for xi in var[0:n]]
            hess = [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
            return np.asarray([[expr.subs([(var[i],X[i]) for i in range(n)]) for expr in hess[j]] for j in range(n)],dtype=float)
    else: 
        return n

func7 = (Helical_Valley,[-1,0,0])
dados.append(func7)



def Bard(numero):
    n = 3
    m = 15
    y = [0.14, 0.18, 0.22, 0.25, 0.29, 0.32, 0.35, 0.39, 0.37, 0.58, 0.73, 0.96, 1.34, 2.10, 4.39]
    u = [i for i in [i+1 for i in range(m)]]
    v = [16-i for i in [i+1 for i in range(m)]]
    w = [min(u[i],v[i]) for i in range(m)]
    fi = [y[i] - (x1 + u[i]/(v[i]*x2 + w[i]*x3)) for i in range(m)]
    função = 0
    for f in fi:
        função = função + f**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func8 = (Bard, [1,1,1])
dados.append(func8)



def Gaussian(numero):
    n = 3
    m = 15
    t = [(8-i)/2 for i in [i+1 for i in range(15)]]
    y = [0.0009,0.0044,0.0175,0.0540,0.1295,0.2420,0.3521,0.3989,0.3521,0.2420,0.1295,0.0540,0.0175,0.0044,0.0009]
    fi = [x1*exp((-x2*(t[i]-x3)**2)/2) - y[i] for i in range(15)]
    função = 0
    for f in fi:
        função = função + f**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func9 = (Gaussian, [0.4,1,0])
dados.append(func9)



def Meyer(numero):
    n = 3
    m = 16
    t = [45+5*i for i in [i+1 for i in range(16)]]
    y = [34780,28610,23650,19630,16370,13720,11540,9744,8621,7030,6005,5147,4427,3820,3307,2872]
    fi = [x1*exp(x2/(t[i]+x3)) - y[i] for i in range(16)]
    função = 0
    for f in fi:
        função = função + f**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func10 = (Meyer,[0.02,4000,250])
dados.append(func10)    
    
    

class MySign(sign):
    def _eval_derivative(self,x):
        return 0
class MyAbs(Abs):
    def _eval_derivative(self, x):
        return Derivative(self.args[0], x, evaluate=True)*MySign(self.args[0])

    
def GulfRaDF(numero):
    n = 3
    m = 10
    t = [i/100 for i in [i+1 for i in range(m)]]
    y = [25+(-50*log(ti))**(2/3) for ti in t]
    fi = [exp((-MyAbs(y[i]-x2)**x3)/x1) - t[i] for i in range(m)]
    função = 0
    for f in fi:
        função = função + f**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func11 = (GulfRaDF, [5,2.5,0.15])
dados.append(func11)
    
    
    
def Box3Dim(numero):
    n = 3
    m = 3
    t = [0.1*i for i in [i+1 for i in range(m)]]
    fi = [exp(-t[i]*x1) - exp(-t[i]*x2) - x3*(exp(-t[i]) - exp(-10*t[i])) for i in range(m)]
    função = 0
    for f in fi:
        função = função + f**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func12 = (Box3Dim, [0,10,20])
dados.append(func12)
    
    
    
def PowellSingular(numero):
    n = 4
    m = 4
    f1 = x1+10*x2
    f2 = (5**(1/2))*(x3-x4)
    f3 = (x2-2*x3)**2
    f4 = (10**(1/3))*(x1-x4)**2
    fi = [f1,f2,f3,f4]
    função = 0
    for f in fi:
        função = função + f**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func13 = (PowellSingular,[3,-1,0,1])
dados.append(func13)



def Wood(numero):
    n = 4
    m = 6
    f1 = 10*(x2-x1**2)
    f2 = 1-x1
    f3 = (90**(1/2))*(x4-x3**2)
    f4 = 1-x3
    f5 = (10**(1/2))*(x2+x4-2)
    f6 = (10**(-1/2))*(x2-x4)
    fi = [f1,f2,f3,f4,f5,f6]
    função = 0
    for f in fi:
        função = função + f**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func14 = (Wood,[-3,-1,-3,-1])
dados.append(func14)




def Kowalik_and_Osborne(numero):
    n = 4
    m = 11
    y = [0.1957,0.1947,0.1735, 0.1600, 0.0844, 0.0627, 0.0456, 0.0342, 0.0323, 0.0235, 0.0246]
    u = [4, 2, 1, 0.5, 0.25, 0.1670, 0.1250, 0.1000, 0.0833, 0.0714, 0.0625]
    fi = [y[i] - (x1*(u[i]**2 + u[i]*x2))/(u[i]**2 + u[i]*x3 + x4) for i in range(m)]
    função = 0
    for f in fi:
        função = função + f**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func15 = (Kowalik_and_Osborne,[0.25,0.39,0.415,0.39])
dados.append(func15)
    
    
    
def Brown_and_Dennis(numero):
    n = 4
    m = 20
    t = [i/5 for i in [i+1 for i in range(m)]]
    fi = [(x1+t[i]*x2 - exp(t[i]))**2 + (x3 + x4*sin(t[i]) - cos(t[i]))**2 for i in range(m)]
    função = 0
    for f in fi:
        função = função + f**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n
    
func16 = (Brown_and_Dennis,[25,5,-5,-1])
dados.append(func16)
    
    

def Osborne1(numero):
    n = 5
    m = 33
    t = [10*(i-1) for i in [i+1 for i in range(m)]]
    ya = [0.844,0.718,0.478,0.908,0.685,0.467,0.932,0.658,0.457,0.936,0.628,0.448,0.925,0.603,0.438,0.908,0.580,0.431,0.881,0.558,0.424,0.850,0.538,0.420,0.818,0.522,0.414,0.784,0.506,0.411,0.751,0.490,0.406]
    y = []
    for i in range(11):
        y.append(ya[3*i])
    for i in range(11):
        y.append(ya[3*i + 1])
    for i in range(11):
        y.append(ya[3*i + 2])
    fi = [y[i] -  (x1 + x2*exp(-t[i]*x4) + x3*exp(-t[i]*x5)) for i in range(m)]
    função = 0
    for f in fi:
        função = função + f**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func17 = (Osborne1,[0.5,1.5,-1,0.01,0.02])
dados.append(func17)



def BiggsEXP6(numero):
    n = 6
    m = 13
    t = [0.1*i for i in [i+1 for i in range(m)]]
    y = [exp(ti) - 5*exp(-10*ti) + 3*exp(-4*ti) for ti in t]
    fi = [x3*exp(-t[i]*x1) - x4*exp(-t[i]*x2) + x6*exp(-t[i]*x5) - y[i] for i in range(m)]
    função = 0
    for f in fi:
        função = função + f**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func18 = (BiggsEXP6,[1,2,1,1,1,1])
dados.append(func18)
    
    
    
def Osborne2(numero):
    n = 11
    m = 65
    t = [(i-1)/10 for i in [i+1 for i in range(m)]]
    y = [1.366, 1.191, 1.112, 1.013, 0.991, 0.885, 0.831, 0.847, 0.786, 0.725, 0.746, 0.679, 0.608, 0.655, 0.616, 0.606, 0.602, 0.626, 0.651, 0.724, 0.649, 0.649, 0.694, 0.644, 0.624, 0.661, 0.612, 0.558, 0.533, 0.495, 0.5, 0.423, 0.395, 0.375, 0.372, 0.391, 0.396, 0.405, 0.428, 0.429, 0.523, 0.562, 0.607, 0.653, 0.672, 0.708, 0.633, 0.668, 0.645, 0.632, 0.591, 0.559, 0.597, 0.625, 0.739, 0.71, 0.729, 0.72, 0.636, 0.581, 0.428, 0.292, 0.162, 0.098, 0.054]
    fi = [y[i] - (x1*exp(-t[i]*x5) + x2*exp((-1)*(t[i] - x9)*(t[i] - x9)*x6) + x3*exp((-1)*(t[i] - x10)*(t[i] - x10)*x7) + x4*exp((-1)*(t[i]*x11)*(t[i]*x11)*x8)) for i in range(m)]
    função = 0
    for f in fi:
        função = função + f**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func19 = (Osborne2,[1.3, 0.65, 0.65, 0.7, 0.6, 3, 5, 7, 2, 4.5, 5.5])
dados.append(func19)
    
    
    
def Watson(numero):
    n = 6
    m = 29
    t = [i/29 for i in [i+1 for i in range(m)]]
    f1 = [[(j-1)*var[j-1]*t[i]**(j-2) for j in [j+1 for j in range(1,n)]] for i in range(m)]
    f2 = [[var[j-1]*t[i]**(j-1) for j in [j+1 for j in range(n)]] for i in range(m)]
    f1i = []
    for i in range(m):
        fk = 0
        for f in f1[i]:
            fk = fk+f
        f1i.append(fk)
    f2i = []
    for i in range(m):
        fk = 0
        for f in f2[i]:
            fk = fk+f
        fk = fk**2
        f2i.append(fk)
    fi = []
    for i in range(m):
        fi.append(f1i[i] - f2i[i] - 1)
    função = 0
    for f in fi:
        função = função + f**2
    função = função + x1**2 + (x2-x1**2 -1)**2

    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

func20 = (Watson,[0,0,0,0,0,0])
dados.append(func20)    

    
    
def ExtendedRosenbrockFunction(numero):
    n = 4
    m = n
    f2i1 = [10*(var[i+1] - var[i]) for i in [2*i for i in range(int(n/2))]]
    f2i2 = [1-var[i-1] for i in [2*(i+1) for i in range(int(n/2))]]    
    fi = []
    for i in range(int(m/2)):
        fi.append(f2i1[i])
        fi.append(f2i2[i])
    função = 0
    for f in fi:
        função = função + f**2
    
    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n    
    
xERF = [-1.2*(((-1)**i)/2 + 1/2) + 1*(((-1)**(i+1))/2 + 1/2) for i in range(ExtendedRosenbrockFunction(4))]    

func21 = (ExtendedRosenbrockFunction,xERF)   
dados.append(func21)
    
    
    
def ExtendedPowellSingularFunction(numero):
    n = 8
    m = n
    f4i1 = [var[i] + 10*var[i+1] for i in [4*i for i in range(int(m/4))]]
    f4i2 = [(5**(1/2))*(var[i+1] - var[i+2]) for i in [4*i+1 for i in range(int(m/4))]]
    f4i3 = [(var[i-1] - 2*var[i])**2 for i in [4*i+2 for i in range(int(m/4))]]
    f4i4 = [(10**(1/2))*(var[i-3] - var[i])**2 for i in [4*i+3 for i in range(int(m/4))]]
    fi = []
    for i in range(int(m/4)):
        fi.append(f4i1[i])
        fi.append(f4i2[i])
        fi.append(f4i3[i])
        fi.append(f4i4[i])
    função = 0
    for f in fi:
        função = função + f**2
    
    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n    
        
xEPS = []
for i in range(ExtendedPowellSingularFunction(4)):
    if i%4 == 0:
        xEPS.append(3)
    elif i%4 == 1:
        xEPS.append(-1)
    elif i%4 == 2:
        xEPS.append(0)
    else:
        xEPS.append(1)
    
func22 = (ExtendedPowellSingularFunction,xEPS)
dados.append(func22)



def Penalty(numero):
    n = 4
    m = n+1
    a = 10**(-5)
    fi = [(a**(1/2))*(var[i-1]-1) for i in [i+1 for i in range(m-1)]]
    fm = -1/4
    for i in range(n):
        fm = fm + var[i]**2
    função = fm**2
    for f in fi:
        função = função + f**2
    
    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n    
     
xPen = [i+1 for i in range(Penalty(4))]

func23 = (Penalty,xPen)
dados.append(func23)    
    
    
    
def PenaltyII(numero):
    n = 4
    m = 2*n
    a = 10**(-5)
    fi = []
    fi.append(x1-0.2)
    asdf = [i for i in range(n)]
    asdf.pop(0)
    for i in asdf:
        fi.append((a**(1/2))*(exp(var[i]/10) + exp(var[i-1]/10) - (exp(i/10) + exp((i-1)/10))))
    for i in asdf:
        fi.append((a**(1/2))*(exp(var[i]/10) - exp(1/10)))
    f2n = 0
    for i in range(n):
        f2n = f2n + (n-(i+1) + 1)*var[i]**2
    fi.append(f2n-1)
    função = 0
    for f in fi:
        função = função + f**2
    
    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n    

xPenII = np.ones(PenaltyII(4))/2
func24 = (PenaltyII,xPenII)
dados.append(func24)



def VariablyDimensioned(numero):
    n = 4
    m = n+2
    fi = []
    for i in range(n):
        fi.append(var[i] - 1)
    fn1 = 0
    for i in range(n):
        fn1 = fn1 + (i+1)*(var[i] - 1)
    fi.append(fn1)
    fn2 = fn1**2
    fi.append(fn2)
    função = 0
    for f in fi:
        função = função + f**2
    
    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n    

xVarD = []
for i in range(VariablyDimensioned(4)):
    xVarD.append(1-((i+1)/VariablyDimensioned(4)))

func25 = (VariablyDimensioned,xVarD)
dados.append(func25)



def Trigonometric(numero):
    n = 4
    m = n
    sumi = 0
    for i in range(n):
        sumi = sumi + cos(var[i])
    fi = [n - sumi + (i+1)*(1-cos(var[i])) - sin(var[i]) for i in range(m)]
    função = 0
    for f in fi:
        função = função + f**2
    
    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n
    
xTrig = np.ones(Trigonometric(4))/Trigonometric(4)

func26 = (Trigonometric,xTrig)
dados.append(func26)

    
    
def BrownAlmostLinear(numero):
    n = 4
    m = n
    sumi = 0
    for i in range(n):
        sumi = sumi + var[i]
    fi = [var[i] + sumi - (n+1) for i in range(m-1)]
    prodi = 1
    for i in range(n):
        prodi = prodi*var[i]
    fi.append(prodi - 1)
    função = 0
    for f in fi:
        função = função + f**2
    
    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n
    
xBAL = np.ones(BrownAlmostLinear(4))/2

func27 = (BrownAlmostLinear,xBAL)
dados.append(func27)
    


def DiscreteBoundaryValue(numero):
    n = 4
    m = n
    var2 = var[0:n]
    var2.append(0)
    h = 1/(n+1)
    t = [i*h for i in [i+1 for i in range(m)]]
    fi = [2*var2[i] - var2[i-1] - var2[i+1] + (h**2)*((var2[i] + t[i] + 1)**3)/2 for i in range(m)]
    função = 0
    for f in fi:
        função = função + f**2
    
    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n
    
h = 1/(DiscreteBoundaryValue(4)+1)
t = [i*h for i in [i+1 for i in range(DiscreteBoundaryValue(4))]]
xDBV = [t[j]*(t[j]-1) for j in range(DiscreteBoundaryValue(4))]

func28 = (DiscreteBoundaryValue,xDBV)
dados.append(func28)



def DiscreteIntegral(numero):
    n = 4
    m = n
    var2 = var[0:n]
    var2.append(0)
    h = 1/(n+1)
    t = [i*h for i in [i+1 for i in range(m)]]
    sumtoi = 0
    sumtoiset = []
    for i in range(m):
        sumtoi = sumtoi + t[i]*(var2[i] + t[i] + 1)**3
        sumtoiset.append(sumtoi)
    sumfromi = 0
    sumfromiset = []
    for i in [m-i-1 for i in range(m)]:
        sumfromi = sumfromi + (1-t[i])*(var2[i] + t[i] + 1)**3
        sumfromiset.append(sumfromi)
    fi = [var[i] + h*((1-t[i])*sumtoiset[i] + t[i]*sumfromiset[m-i-1])/2 for i in range(m)]
    função = 0
    for f in fi:
        função = função + f**2
    
    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

h = 1/(DiscreteIntegral(4)+1)
t = [i*h for i in [i+1 for i in range(DiscreteIntegral(4))]]
xDI = [t[j]*(t[j]-1) for j in range(DiscreteIntegral(4))]
   
func29 = (DiscreteIntegral,xDI)
dados.append(func29)



def BroydenTridiagonal(numero):
    n = 4
    m = n
    var2 = var[0:n]
    var2.append(0)
    fi = [(3-2*var2[i])*var2[i] - var2[i-1] - 2*var2[i+1] + 1 for i in range(m)]
    função = 0
    for f in fi:
        função = função + f**2
    
    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

xBrTr = -np.ones(BroydenTridiagonal(4))

func30 = (BroydenTridiagonal,xBrTr)
dados.append(func30)   



def BroydenBanded(numero):
    n = 4
    m = n
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def LinearFunctionFR(numero):
    n = 4
    m = 6
    sumi = 0
    for i in range(n):
        sumi = sumi + var[i]
    fi = [var[i] - (2/m)*sumi - 1 for i in range(n)]
    for i in range(m-n):
        fi.append(-(2/m)*sumi - 1)
    função = 0
    for f in fi:
        função = função + f**2
    
    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n

xLFFR = np.ones(LinearFunctionFR(4))
func32 = (LinearFunctionFR,xLFFR)    
dados.append(func32)
    
    

def LinearFunctionRO(numero):
    n = 4
    m = 6
    sumi = 0
    for i in range(n):
        sumi = sumi + (i+1)*var[i]
    fi = [(i+1)*sumi - 1 for i in range(m)]
    função = 0
    for f in fi:
        função = função + f**2
    
    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n
    
xLFRO = np.ones(LinearFunctionRO(4))
func33 = (LinearFunctionRO,xLFRO)
dados.append(func33)



def LinearFunctionROwzcar(numero):
    n = 4
    m = 6
    sumi = 0
    for i in range(1,n-1):
        sumi = sumi + (i+1)*var[i]
    fi = [(i+1)*sumi - 1 for i in range(m-2)]
    fi.append(-1)
    função = (-1)**2
    for f in fi:
        função = função + f**2
    
    if numero == 0:
        return função
    elif numero == 1:
        return [diff(função,xi) for xi in var[0:n]]
    elif numero == 2:
        grad = [diff(função,xi) for xi in var[0:n]]
        return [[diff(grad[i],xi) for xi in var[0:n]] for i in range(n)]
    else:
        return n    

xLFROwzcar = np.ones(LinearFunctionROwzcar(4))
func34 = (LinearFunctionROwzcar,xLFROwzcar)
dados.append(func34)
















