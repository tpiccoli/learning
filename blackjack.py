# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 13:33:20 2022

@author: Tiago Piccoli

Projeto 2 - Blackjack!

Aqui estão os requisitos:

Você precisa criar um jogo BlackJack baseado em texto.
O jogo precisa ter um jogador versus um dealer automatizado.
O jogador pode esperar ou pedir mais cartas.
O jogador deve poder escolher o seu valor de apostas.
Você precisa acompanhar o dinheiro total dos jogadores.
Você precisa alertar o jogador de vitórias, perdas, etc ...
"""

import random
#import numpy as np

values = {'p_as':(1,11), 'p2':2, 'p3':3, 'p4':4, 'p5':5, 'p6':6, 'p7':7, 'p8':8, 'p9':9, 'p10':10, 'p_j':10, 'p_q':10, 'p_k':10,
          'o_as':(1,11), 'o2':2, 'o3':3, 'o4':4, 'o5':5, 'o6':6, 'o7':7, 'o8':8, 'o9':9, 'o10':10, 'o_j':10, 'o_q':10, 'o_k':10,
          'c_as':(1,11), 'c2':2, 'c3':3, 'c4':4, 'c5':5, 'c6':6, 'c7':7, 'c8':8, 'c9':9, 'c10':10, 'c_j':10, 'c_q':10, 'c_k':10,
          'e_as':(1,11), 'e2':2, 'e3':3, 'e4':4, 'e5':5, 'e6':6, 'e7':7, 'e8':8, 'e9':9, 'e10':10, 'e_j':10, 'e_q':10, 'e_k':10}

paus=['p_as', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8','p9','p10', 'p_j', 'p_q','p_k']
ouro=['o_as', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8', 'o9','o10', 'o_j', 'o_q', 'o_k']
copas=['c_as', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9','c10', 'c_j', 'c_q', 'c_k']
espadas=['e_as', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9','e10', 'e_j', 'e_q', 'e_k']

baralho=[] #cartas disponíveis no baralho
baralho= paus+ouro+copas+espadas

p1=[] #mão do player 1
p1_pontos=[] #pontos das cartas na mão do player 1
dealer=[] #mão do dealer
dealer_pontos=[] #pontos das cartas na mão do dealer
bar_pos=[] #cartas já pescadas
bar_len=51

p1_wallet=0 #dinheiro disponível para aposta
p1_aposta=0 #dinheiro apostado na rodada

#-----------------------------------
def pescar_p1():
    global bar_len
    while True:
        a=random.randint(0,51)
        if a in bar_pos: #verifica se carta já foi pescada
            pass    
        else:
            try:
                carta=baralho.pop(a)
                p1.append(carta)
                bar_pos.append(a)
                break
            except:
                pass
#-----------------------------------
def pescar_dealer():
    global bar_len
    while True:
        a=random.randint(0,51)
        if a in bar_pos: #verifica se carta já foi pescada
            pass    
        else:
            try:
                carta=baralho.pop(a)
                dealer.append(carta)
                bar_pos.append(a)
                #bar_len=bar_len-1
                break
            except:
                pass
 #-----------------------------------           
def verificador():
    global p1_wallet
    global p1_aposta
    global game
    global soma_p1
    global soma_dealer
    global venc
    global bar_len
    
    p1_pontos.clear()
    dealer_pontos.clear()
    
    for carta in p1:#pego todas as cartas na mão e consulto cada uma no dicionário.
        if carta=='p_as' or carta=='o_as' or carta=='c_as' or carta=='e_as': #se a carta for um ás
            if 'p_j' or 'p_q' or 'p_k' or 'o_j'or'o_q'or'o_k'or' c_j' or 'c_q' or 'c_k' or 'e_j' or 'e_q' or 'e_k' or 'p_as' or 'o_as' or 'c_as' or 'e_as' in p1:#já tiver carta de 10 pts.
                p1_pontos.append(values[carta][0])
            else:
                pass
        if carta=='p_as' or carta=='o_as' or carta=='c_as' or carta=='e_as': #se a carta for um ás
            if 'p_j' or 'p_q' or 'p_k' or 'o_j'or'o_q'or'o_k'or' c_j' or 'c_q' or 'c_k' or 'e_j' or 'e_q' or 'e_k' not in p1:#não tiver carta de 10 pts. 
                p1_pontos.append(values[carta][1])
            else:
                pass
        else: 
            pontos=values[carta]  #cada carta retorna um valor
            p1_pontos.append(pontos) #valor da carta adiciona na lista de pontos do jogador
    
    for carta in dealer:
        if carta=='p_as' or carta=='o_as' or carta=='c_as' or carta=='e_as': #se a carta for um ás
            if 'p_j' or 'p_q' or 'p_k' or 'o_j'or'o_q'or'o_k'or' c_j' or 'c_q' or 'c_k' or 'e_j' or 'e_q' or 'e_k' or 'p_as' or 'o_as' or 'c_as' or 'e_as' in p1:#já tiver carta de 10 pts.
                dealer_pontos.append(values[carta][0])
            else:
                pass
        if carta=='p_as' or carta=='o_as' or carta=='c_as' or carta=='e_as': #se a carta for um ás
            if 'p_j' or 'p_q' or 'p_k' or 'o_j'or'o_q'or'o_k'or' c_j' or 'c_q' or 'c_k' or 'e_j' or 'e_q' or 'e_k' not in p1:#não tiver carta de 10 pts. 
                dealer_pontos.append(values[carta][1])
            else:
                pass
        else: 
            pontos=values[carta]  #cada carta retorna um valor
            dealer_pontos.append(pontos) #valor da carta adiciona na lista de pontos do jogador

        #pontos=values[carta]
        #dealer_pontos.append(pontos)
     
    soma_p1 = sum(p1_pontos) #soma de pontos da mão do jogador
    soma_dealer = sum(dealer_pontos)

    if soma_p1==21 and soma_dealer==21 or soma_p1>21 and soma_dealer>21:
        print('Temos um EMPATE!')
        p1_wallet= p1_wallet + p1_aposta
        p1_aposta=0
        venc=1
    
    elif soma_p1 == 21:
        print('BLACKJACK! Parabéns, você venceu a rodada!')
        p1_wallet = 1.5*p1_aposta + p1_wallet
        p1_aposta = 0
        venc=1
        
    elif soma_dealer == 21:
        print('Dealer BLACKJACK, você perdeu.')
        p1_aposta=0
        venc=1
        
    elif soma_p1>21:   
        print("Sua mão ultrapassou 21 pontos, lamento mas você perdeu a rodada.")
        p1_aposta=0
        venc=1

    elif soma_dealer>21:
        print('Dealer estourou, você venceu!')
        p1_wallet = 1.5*p1_aposta + p1_wallet
        p1_aposta = 0
        venc=1
        
    elif soma_p1>soma_dealer and soma_p1<=21 and soma_dealer>17:
        print('Você venceu!')
        p1_wallet = 1.5*p1_aposta + p1_wallet
        p1_aposta = 0
        venc=1
        
    elif len(dealer)==5 and soma_dealer==17 and soma_p1<=21:
        print('Dealer bateu, você venceu!')
        p1_wallet = 1.5*p1_aposta + p1_wallet
        p1_aposta = 0
        venc=1
 
    elif soma_dealer==17:
        print('Temos um EMPATE!')
        p1_wallet= p1_wallet + p1_aposta
        p1_aposta=0
        venc=1

    else:
        print('Ainda não há vencedores, segue o jogo!')
        #game=+1
    #game= game-1
    print('--------------------')
    print('Cartas dealer:',dealer)
    print('Cartas jogador:',p1)
    print('Pontos na mão do Dealer:', soma_dealer)
    print('Pontos na mão do jogador:', soma_p1)
    print('--------------------')
   
#-------------------------------------------------------------------------------
        
#inicio do jogo - código 

#aporte para apostas
  
game=0 #contagem de rodadas

p1_wallet= int(input('Jogador, por favor coloque a quantia fictícia de dinheiro para realizar as apostas:R$'))
game=int(input('Jogador, digite em quantas rodadas quer participar (1-10):'))  

while game > 0:

    p1_aposta=int(input('Por favor, faça a aposta para esta rodada:'))
    p1_wallet= p1_wallet - p1_aposta
    
    for _ in range(2):
        pescar_p1()
        pescar_dealer()
    
    #preciso saber se tem um ás
    #mostrar 1 carta do dealer e as cartas do jogador
    print("Uma carta do Dealer: ",dealer[0])
    print("Cartas do jogador: ", p1)
    print('--------------------')
    hit=int(input('Jogador, digite "1" caso deseje pescar uma carta ou "2" caso não queira.'))
    if hit==1:
        pescar_p1()
    
    venc=0    
    verificador() #se tem um vencedor, a rodada encerra.
    
    while venc==0: #roda jogadas subsequentes 
        hit=int(input('Jogador, digite "1" caso deseje pescar uma carta ou "2" caso não queira.'))
        if hit==1:
            pescar_p1()
        if soma_dealer<17:
            pescar_dealer()
        else:
            pescar_dealer()
        verificador()
        #não tem vencedor, o jogo deve continuar
    print('Saldo (R$):', p1_wallet)
    game=game-1
    dealer.clear()
    p1.clear()
 
'''
bloco de anotações

paus=(p_as, p2, p3, p4, p5, p6, p7, p8, p9, p_j, p_q, p_k)
ouro=(o_as, o2, o3, o4, o5, o6, o7, o8, o9, o_j, o_q, o_k)
copas=(c_as, c2, c3, c4, c5, c6, c7, c8, c9, c_j, c_q, c_k)
espadas=(e_as, e2, e3, e4, e5, e6, e7, e8, e9, e_j, e_q, e_k)
 #-----------------------------------       
def as_value():
    if 'p_as' or 'o_as' or ' c_as' or 'e_as' in p1: #ver se tem ás em p1
        if 'p_j' or 'p_q' or 'p_k' or 'o_j'or'o_q'or'o_k'or' c_j' or 'c_q' or 'c_k' or 'e_j' or 'e_q' or 'e_k' in p1: #se tem alguma carta de 10 pts na mão
            p1_pontos.append(-10)
    if 'p_as' or 'o_as' or ' c_as' or 'e_as' in dealer: #ver se tem ás
        if 'p_j' or 'p_q' or 'p_k' or 'o_j'or'o_q'or'o_k'or' c_j' or 'c_q' or 'c_k' or 'e_j' or 'e_q' or 'e_k' in dealer: #se tem alguma carta de 10 pts na mão
            dealer_pontos.append(-10) 
-------------------------
       if soma_p1==2: #significa que tem dois ases.
        p1_pontos.append(-10)
    if soma_dealer==2:
        dealer_pontos.append(-10)         
            
'''