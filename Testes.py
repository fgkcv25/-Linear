# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 18:21:42 2019

@author: CLIENTE
"""

import time
import numpy as np
from Funções import dados
from Método_do_Gradiente import MétodoDoGradiente as MG
from Método_de_Newton import MétodoDeNewton as MN
from Método_Quasi_Newton_BFGS import MétodoQuasiNewtonBFGS as BFGS
from Método_de_Região_de_Confiança import MétodoDeRegiãoDeConfiança as RDC
from Método_de_Gradiente_Conjugado import MétodoDeGradienteConjugado as MGC

lista = [MG,MN,BFGS,RDC,MGC]


#cria o negócio que vai ter todas os dados necessários das funções já disponível
#para todos os métodos acessarem sem precisar calcular toda vez

dados2 = dados

DATA = [[dado[0](num) for num in range(4)] for dado in dados2]
DATA2 = [dado[1] for dado in dados2]
DATA3 = [dado[0].__name__ for dado in dados2]
for i in range(len(DATA)):
    DATA[i].append(DATA2[i])
    DATA[i].append(DATA3[i])

#quadratica pra teste
from quad import quad
QUAD = [quad[0](num) for num in range(4)]
QUAD.append(quad[1])





sucesses = []

for método in lista:
    k = 0
    j = 0
    print(método.__name__)
    for dado in DATA:
        k = k+1
        print('\u001b[37;1m')
        print(k)
        print(dado[5])
        effer = método(dado)
        if np.dot(effer[2],effer[2]) < 10**(-4):
            print('\u001b[32;1m Yes!')
            print('\u001b[37;1m Valor do ponto:')
            print(effer[0])
            print('Valor da função:')
            print(effer[1])
            j = j+1
        else:
            print('\u001b[31m NO!')
    print('\u001b[37;1m')
    print('')
    sucesses.append(j)

print(sucesses)
print(len(lista))




