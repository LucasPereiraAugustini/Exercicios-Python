"""
Desafio 103

Problema: Faça um programa que tenha uma função chamada ficha(), que receba
          dois parâmetros opcionais: o nome de um jogador e quantos gols ele
          marcou.
          O programa deverá ser capaz de mostrar a ficha do jogador, mesmo
          que algum dado não tenha sido informado corretamente.

Resolução do problema:
"""


# Realiza a impressão da ficha do jogador
def ficha(nome_jogador='<desconhecido>', qtd_gols=0):
    print(f'O jogador {nome_jogador} fez {qtd_gols} gol(s) no campeonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('Quantidade de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(qtd_gols=gols)
else:
    ficha(nome, gols)
