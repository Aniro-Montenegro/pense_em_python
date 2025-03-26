import random

# Gera 30 números únicos de 6 dígitos
numeros_unicos = random.sample(range(100000, 1000000), 30)
i=0
while i<30:
    numeros_unicos.append(numeros_unicos[i])
    i=i+4
 

numeros_unicos+=[123456,123457]

senhas=set()

for n in numeros_unicos:
    senhas.add(n)
   
dicionario_contagem=dict()
for n in senhas:
    if str(n) in dicionario_contagem:
        dicionario_contagem[str(n)]+=1
    else:
        dicionario_contagem[str(n)]=1

for chave in dicionario_contagem.keys():
    print(f'{chave}:{dicionario_contagem[chave]}')




