# Função é uma sequencia nomeada de instrucoes que executa uma operacao de computacao.
#Chamada de funcao
x=type(42)
print(x)
z=type(type)
print(z)
# Uma funcao pode ou nao ter retorno

def soma(x,y):
    return x+y
def soma2(x,y):
    print(x+y)

soma(10,10)
soma2(20,20)
s=soma(5,5)
print(s)

#O Python oferece funcoes que convertem valores de um tipo em outro
x=4.52
print(type(x),x)
x=int(x)
print(type(x),x)
x=str(x)
print(type(x),x)

#Funcoes matematicas
# Modulo matematico é um arquivo que contem coleção de funções relacionadas a calculos matematicos
import math

x=math.pi
print(x)

#Funcao que calcula o fatorial de um numero
def fatorial(n):
    if n==0 or n==1:
        return n
    else:
        return n * fatorial(n-1)
x=fatorial(5)
print(x)

#Funcao que recebe dois nuros e calcula a exponenciacao deste numero

def exponenciacao(base, expoente):
    if expoente == 0:
        return 1
    elif expoente == 1:
        return base
    else:
        return base * exponenciacao(base, expoente - 1)
print(exponenciacao(2, 3))  # Saída: 8
print(exponenciacao(5, 0))  # Saída: 1

#variaveis e parametros locais. 

def concatenacao(palavra1,palavra2):
    return f'{palavra1} {palavra2}'

print(concatenacao("Parabens","Amigo"))
# palavra 1 e palavra2 sao parametros
# "Parabens" e "Amigo" sao argumentos

#Se descomentar o codigo abaixo vai reparar que nao vai funcionar, pois palavra1 nao faz parte deste escopo
# try:
#     print(palavra1)
# except ValueError:
#     print(ValueError)
