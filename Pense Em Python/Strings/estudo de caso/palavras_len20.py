arq=open("Strings/estudo de caso/criptografia.txt")
palavras_len20_set=set()
palavras_len20_lista=[]
for linha in arq:
    linha=linha.replace(","," ")
    lista=linha.split(" ")
    for p in lista:
        p=p.strip()
        if len(p)>=20:            
            palavras_len20_lista.append(p)
            
palavras_len20_lista.sort()
for p in palavras_len20_lista:
    palavras_len20_set.add(p)


print(palavras_len20_set)
print(palavras_len20_lista)