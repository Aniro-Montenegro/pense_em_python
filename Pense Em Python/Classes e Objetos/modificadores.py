
def inverte_string(palavra):    
    nova_palavra=palavra[::-1]
    return nova_palavra


print(inverte_string("Boa noite e boa sorte"))


def inverte_lista_modificador(lista):  

    nova_lista=lista[::-1]
    lista=[]
    for n in nova_lista:
        lista.append(n)
    return lista

lista=[1,2,3,4,5,6,7,8,9]

lista=inverte_lista_modificador(lista=lista)
print(lista)