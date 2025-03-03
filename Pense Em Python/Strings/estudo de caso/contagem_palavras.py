arq=open("Strings/estudo de caso/criptografia.txt","r")
frases=[]
contagem={}
for f in arq:
    frases.append(f)

for frases in frases:
    lista=frases.strip().split(" ")
    for ff in lista:
        if ff not in contagem:
            contagem[ff]=1
        else:
            contagem[ff]=contagem[ff]+1

lista_final=[]
lista_intermediaria={}

for a in contagem:
    lista_intermediaria[a]=contagem[a]


dicionario_ordenado = dict(sorted(lista_intermediaria.items(), key=lambda item: item[1],reverse=True))

print(dicionario_ordenado)

