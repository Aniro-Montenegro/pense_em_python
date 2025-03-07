

import texto as texto_importado  

def most_frequencie(texto, palavra):
    palavra_ordenada = sorted(palavra) 
    palavras_texto = texto.split() 
    dicionario={}
    for l in palavra_ordenada:
        dicionario[l]=0
        for p in palavras_texto:
            for c in p:
                if c in dicionario:
                    dicionario[c]+=1
    itens=dicionario.items()
    for letra,quamtidade in sorted(itens):
        print(letra,":",quamtidade)


# most_frequencie(texto_importado.texto, "aeioucbgd") 


def anagramas(texto):
    palavras_texto = texto.split() 
    i=0
    p=0
    listas=[]
    while i<len(palavras_texto)-1:
        palavra=palavras_texto[i]
        p=i+1
        i+=1
        while p<len(palavras_texto):
            palavras_set=set()
            palavra2=palavras_texto[p]            
            if sorted(palavra) == sorted(palavra2) and palavra!=palavra2:
                palavras_set.add(palavra)
                palavras_set.add(palavra2)
                listas.append(palavras_set)
            p+=1
    print(listas)
        


    

anagramas(texto_importado.texto)