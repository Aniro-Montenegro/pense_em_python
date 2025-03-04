carro={"Onix":100000}

def muda_valor():
    carro=={"Passat":25000}
muda_valor()
print(carro)
# o valor de carro nao muda pois nao faz parte do escopo da funcao muda_valor
# para mudar o valor da variavel global, ela precisa ser declarada dentro da funcao
def muda_valor():
    global carro
    carro={"Passat":25000}
muda_valor()
print(carro)

#outra forma de mudar o valor
def muda_valor(dicionario):
    dicionario={"Gol":458965}
    return dicionario

carro=muda_valor(carro)
print(carro)
