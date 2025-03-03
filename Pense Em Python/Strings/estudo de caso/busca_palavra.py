



def lista_palavras():
    arq=open("Strings/estudo de caso/criptografia.txt","r")
    frases=[]
    palavras=[]
    for f in arq:
        f=f.replace(",","").replace(".","").replace("\n","")
        frases.append(f)

    for frase in frases:
        lista=frase.split(" ")
        palavras+=lista

    return palavras


def busca_palavra(palavras,palavra):  
    
    if len(palavras)==0:
        return f"Palavra {palavra} nao encontrada"
    if len(palavras)==1:
        if palavras[0]==palavra:
            return f"Palavra: {palavra} encontrada "
        else:
            return f"Palavra: {palavra} nao encontrada "
    if len(palavras)==2:
        if palavras[0]==palavra or palavras[1]==palavra:
            return f"Palavra: {palavra} encontrada "
        else:
            return f"Palavra: {palavra} nao encontrada "
   
    elif (palavras[0]==palavra):
        
        return f"Palavra: {palavra} encontrada "
    else:
        return busca_palavra(palavras[1:],palavra)


palavras=lista_palavras()
resultado=busca_palavra(palavras,"complexo")
print(resultado)