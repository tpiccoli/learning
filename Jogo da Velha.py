# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 09:54:23 2022

@author: Tiago Piccoli

JOGO DA VELHA

"""
import numpy as np
        
def verificador():
    
    global res
    
    l1=[tab[0][0],tab[0][1],tab[0][2]]
    l2=[tab[1][0],tab[1][1],tab[1][2]]
    l3=[tab[2][0],tab[2][1],tab[2][2]]
    c1=[tab[0][0],tab[1][0],tab[2][0]]
    c2=[tab[0][1],tab[1][1],tab[2][1]]
    c3=[tab[0][2],tab[1][2],tab[2][2]]
    d1=[tab[0][0],tab[1][1],tab[2][2]]
    d2=[tab[0][2],tab[1][1],tab[2][0]]   

    #print(l1,l2,l3,c1,c2,c3)
    print('-------------')
    mat_resp=[l1,l2,l3,c1,c2,c3,d1,d2]

    
    for lr in mat_resp:
        for lr1 in lr:
                       
            result1=all(lr1 == 1 for lr1 in lr)
            result2=all(lr1 == 2 for lr1 in lr)
            if result1:
                res=1
                break
            elif result2:
                res=2
                break


p1= str(input('Digite o nome do jogador 1:')) #circulo como 1 
p2= str(input('Digite o nome do jogador 2:')) #xis como 2 
print('-------------')
print(p1,' jogará com os círculos, representado na matriz como 1')
print(p2,' jogará com os xis, representado na matriz como 2')
print('-------------')
print('COMO JOGAR? \n Cada jogador irá digitar, RESPECTIVAMENTE, a linha desejada (1-3) e a coluna desejada (1-3) \n Digitando somente o número quando solicitado')
print('-------------')
#tab=[['-','-','-'],['-','-','-'],['-','-','-']]

tab=np.zeros((3,3))
n_jog=0
res=0
spaces=[]

while n_jog<=8 and res==0:
    while True:
        p1_row = int(input('Jogador 1, digite a sua jogada:\n Linha desejada:'))
        p1_col = int(input('Coluna desejada:'))
        j1=(p1_row,p1_col)
        if n_jog==5: #resultado como empate, já que foram preenchidas todas as 9 casas, mas o verificador irá rodar e caso haja um vencedor será desconsiderado
            res=3
        if j1 in spaces: #verifica se a jogada já foi realizada em algum momento
            print('Jogue novamente, posição já marcada')
        else:
            spaces.append(j1)#armazena a jogada
            verificador()
            break
    
    n_jog += 1 #conta a jogada como válida
    tab[p1_row-1, p1_col-1]=1 #converte posição 1-2-3 para 0-1-2
    print(tab)
    verificador()
    
    if n_jog==9:
        break
    
    while True and res==0: #redundância, linha 74 executa o and res!=0. Não alterado, para fins didáticos.
        p2_row = int(input('Jogador 2, digite a sua jogada:\n Linha desejada:'))
        p2_col = int(input('Coluna desejada:'))
        j2=(p2_row,p2_col)
        if j2 in spaces:
                print('Jogue novamente, posição já marcada')
        else:
            spaces.append(j2)
            verificador()
            break
        
    n_jog += 1
    tab[p2_row-1, p2_col-1]=2
    print(tab)
    verificador()
    
    if res==3 or res!=0:
        break

    
if res==1:
    print('Parabéns! o Jogador',p1,'venceu!')
elif res==2:
    print('Parabéns! o Jogador',p2,'venceu!')
elif res==3:
    print('Empate!')    
else:
    print('Empate!')    



#verificador
'''if n_jog>=3: #condição para rodar o verificador
    p1_jog=0

if p1_row==1:
    p1_jog=p1_col-1
elif p1_row==2:
    p1_jog=p1_row+p1_col
elif p1_row==3:
    p1_jog=p1_row+p1_col+2

tab.insert('O',p1_jog)
n_jog += 1
print(tab)

    for lr in mat_resp: #VERIFICAR, ERRO ESTÁ AQUI
        if sum(lr)==3.0: 
            if lr==0: #devo verificar se há zero em algum valor de l1 
                res=0
            else: 
                res=1
        elif sum(lr)==6.0:
            if lr==0:    
                res=0
            else:
                res=2

'''