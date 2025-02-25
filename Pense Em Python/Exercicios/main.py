from base import ordem_operacoes_base
import random
import os

lista = list(ordem_operacoes_base.ordem_operacoes_base_dicionario.keys())

pontos = 0
while True:
    print("Digite o resultado da operacao ou -1 para sair")
    item_aleatorio = random.choice(lista)
    print(item_aleatorio)
    
    resultado = input()
    os.system('clear')
    
    if resultado == "-1":
        break
    

    if not resultado.isdigit() and not (resultado.startswith('-') and resultado[1:].isdigit()):
        print("Por favor, digite um número válido!")
        continue

    if ordem_operacoes_base.ordem_operacoes_base_dicionario[item_aleatorio] == int(resultado):
        pontos += int(resultado)
        print("*******")
        print("Acertou")
        print("*******")
        print("Pontos: ", pontos)
        print("*******\n")
    else:
        pontos -= int(resultado)
        print("*******")
        print("Errou")
        print("*******")
        print("Pontos: ", pontos)
        print("*******\n")
