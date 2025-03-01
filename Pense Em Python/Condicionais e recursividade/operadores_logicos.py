import time

#and or not

def isPar(numero):
    return numero%2==0

print(isPar(4))

def idadeTrabalho(idade):
    if idade>=18 and idade <=60:
        print("Idade para trabalhar")
    elif  idade<18:
        print("Menor de idade")
    elif idade>60:
        print("Aposentado")

def surpresa(booleano):
    print(not booleano)
## numero inteiros sao True em python

print(10 and True)
print(0 and True)
print(-10 and True)

def paga_ou_gratis():
    n=0
    z=0
    while(n!=-1 and z!=-1):
        print("Escolha o numero correspondente")
        print("-1 para sair")
        print("**************************************************************")
        print("**************************************************************")
        print("**************************************************************")
        print("1- Tenho o dinheiro suficiente")
        print("2- Nao Tenho o dinheiro suficiente")
        n=int(input())
        print("**************************************************************")
        print("1- Esta de graça")
        print("2- Nao Esta de graça")
        z=int(input())
        if n==1 or z==1:         
            print("**************************************************************")
            print("**********************Pode passar*****************************")
            print("**************************************************************\n\n")          
        if z==2 and n==2:         
            print("**************************************************************")
            print("**********************Nao deu*********************************")
            print("**************************************************************\n\n")
         
# paga_ou_gratis()



def verifica_primo(numero):
    divisores=0
    
    if numero==2:
        print("É primo")
    elif numero%2==0:
        print("Nao é primo")

    elif numero==1:
        print("Nao é primo")
    else:
        n=numero
        while n>0:
            if numero%n==0:
                divisores+=1
            n-=1
        if divisores==2:
            print("É primo")
        else:
            print("Nao é primo")

verifica_primo(2)
        
def lancamento(contador):
    if contador<=0:
        print("Decolou!!")
    else:
        print(contador)       
        time.sleep(1)
        lancamento(contador-1)
lancamento(10)

