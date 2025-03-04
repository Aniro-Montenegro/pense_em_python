

#Reducao
t=[1,2,3,4]
def add_all(t):
    total=0
    for x in t:
        total+=x
    return total

print(add_all(t))
#a funcao acima percorre a lista somando cada valor em uma variavel

#faz a emsma coisa que add_all
soma=sum(t)
print(soma)
soma=sum(t,start=10)
print(soma)
nomes = ["Alice", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia"]
#nao intera com strings
# soma_nomes=sum(nomes)
# print(soma_nomes)

# mapeamento - mapeia uma funcao para cada elemeto da lista

def upper_case(lista_nomes):
    lista=[]
    for n in lista_nomes:
        lista.append(n.upper())
    return lista

lista_capitalizada=upper_case(nomes)
print(lista_capitalizada)


#filtragem

def strngs_len5(lista_nomes):
    lista=[]
    for s in lista_nomes:
        if len(s)>=5:
            lista.append(s)
    return lista