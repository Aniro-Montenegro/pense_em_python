lista_numeros=[100,25,36,58,47,96,54,12,3,0]


def menor_maior(lista):
    maior=lista[0]
    menor=lista[0]
 
    for i in lista:
        if i>maior:
            maior=i
        if i<menor:
            menor=i
    return menor,maior


menor,maior=menor_maior(lista_numeros)
print(menor,maior)