s='banana'
lista=list(s)
def delete_caracteres(lista):
    del lista[0]

delete_caracteres(lista)
print(lista)

lista1=[1,2,3,4,5]
lista2=[6,7,8]
endereco_memoria_lista1 = id(lista1)
endereco_memoria_lista2 = id(lista2)
lista1.append(90)
endereco_memoria_lista1_append = id(lista1)
lista2=lista2+[25]
endereco_memoria_lista2_append = id(lista2)
print(endereco_memoria_lista1)
print(endereco_memoria_lista2)
print(endereco_memoria_lista1_append)
print(endereco_memoria_lista2_append)
#append altera a lista o operador + cria outra lista

