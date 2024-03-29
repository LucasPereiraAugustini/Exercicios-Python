"""
Desafio 104

Problema: Crie um programa que tenha a função leiaint(), que vai funcionar de forma
          semelhante a função input() do python, só que fazendo a validação para aceitar
          apenas um valor númerico.

          Ex:
            n = leiaint('Digite um n: ')

Resolução do problema:
"""


def leiaint(msg):
    valor = str(input(msg).strip())
    while not valor.isnumeric():
        print('\033[31mERRO! Informe um valor inteiro corretamente...\033[m')
        valor = str(input(msg).strip())
    return valor


n = leiaint('Digite um número: ')
print(f'Você digitou o número: {n}')
