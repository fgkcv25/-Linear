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

#lista dos métodos para testar
lista = [MG,MN,BFGS,RDC,MGC]

#esta linha usei para testar funções sem percorrer tudo, com dados[4:6], por exemplo
dados2 = dados

#cria uma lista de todos os dados necessários das funções já disponível
#para todos os métodos acessarem sem precisar calcular toda vez
DATA = [[dado[0](num) for num in range(4)] for dado in dados2]
DATA2 = [dado[1] for dado in dados2]
DATA3 = [dado[0].__name__ for dado in dados2]
for i in range(len(DATA)):
    DATA[i].append(DATA2[i])
    DATA[i].append(DATA3[i])



#testo cada método e dou informações sobre o ponto, a função, a convergência e o método
names = [dado[5] for dado in DATA]
sucesslist = []
tempototal = []

for método in lista:
    t0 = time.time()
    k = 0
    sucesses = []
    print(método.__name__)
    for dado in DATA:
        k = k+1
        print('\u001b[37;1m')
        print(k)
        print(dado[5])
        effer = método(dado)
        if np.dot(effer[2],effer[2]) < 10**(-4):
            print('\u001b[32;1m Convergiu!')
            print('\u001b[37;1m Ponto:')
            print(effer[0])
            print('Valor da função:')
            print(effer[1])
            j = DATA.index(dado)
            sucesses.append(j)
        else:
            print('\u001b[31m Não convergiu.')
    print('\u001b[37;1m')
    print('')
    sucesslist.append(sucesses)
    tempototal.append(time.time() - t0)



numberofsucessess = [len(dado) for dado in sucesslist]
#mostro a quantidade de sucessos em cada método na ordem descrita em 'lista'
print(numberofsucessess)
#mostro a quantidade de funções testadas
print(len(DATA))
#mostra o tempo que cada método, em ordem, levou para percorrer todas as funções teste
print(tempototal)



#pode também verificar na lista sucesslist quais funções tiveram sucesso em qual método
#e checar cada número na lista names para saber a função correspondente
