while(True):
    arq=open("Strings/estudo de caso/criptografia.txt")
    x=int(input('Digite o numro de caractres do tamanho desejado ou -1 para sair\n'))
    if x==-1:
        break
    palavras_lenx_set=set()
    palavras_lenx_lista=[]
    for linha in arq:
        linha=linha.replace(","," ")
        lista=linha.split(" ")
        for p in lista:
            p=p.strip()
            if len(p)==x:
                palavras_lenx_lista.append(p)
            
        palavras_lenx_lista.sort()
        for p in palavras_lenx_lista:
            palavras_lenx_set.add(p)


    print(palavras_lenx_set)
    print(palavras_lenx_lista)