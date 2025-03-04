lista_aninhada=[[1,2],[3,4],[5,6]]




def nested_sum(lista):
    total=0
    for l in lista:
        for ll in l:
            if type(ll) ==int:
                total+=ll
    return total

soma=nested_sum(lista_aninhada)
print(soma)


def cumsum(lista):
    nova_lista=[]
    total=0
    for l in lista:
        total+=l
        nova_lista.append(total)
    return nova_lista
lista_numeros=[1,2,3]
soma_aucumulada_lista=cumsum(lista_numeros)
print(soma_aucumulada_lista)

lista_numeros=[1,2,3,4,5,6,7]
def middle(lista):
    lista.pop(0)
    lista.pop(len(lista)-1)
    return lista

print(middle(lista_numeros))

def is_sorted(lista):
    i=0
    while(i<(len(lista)-1)):
        if lista[i]>lista[i+1]:
            return False
        i+=1
    return True


print(is_sorted(lista_numeros))
lista_numeros=lista_numeros+[45,10]
print(is_sorted(lista_numeros))


def has_duplicates(lista):
    i=0
    lista.sort()
    while(i<(len(lista)-1)):
        if lista[i]==lista[i+1]:
            return True
        i+=1
    return False
print(has_duplicates(lista_numeros))
        
lista_numeros=lista_numeros+[14,25,36,458,14]
print(has_duplicates(lista_numeros))

def busca_binaria(lista, elemento):
    tamanho=len(lista)
    if tamanho==1 or tamanho==2:
        return elemento in lista
    else:
        metade=tamanho//2
        if lista[metade]<elemento:
            nova_lista=lista[metade:]
            return busca_binaria(nova_lista,elemento)
        elif lista[metade]>elemento:
            nova_lista=lista[:metade]
            return busca_binaria(nova_lista,elemento)


retorno=busca_binaria(lista_numeros,12222)
print(retorno)