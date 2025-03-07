#Tuplas sao parecidas com as listas, porem são imutáveis.
tupla='a','e','i','o','u'
print(type(tupla))
print(tupla)
consoantes = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

print(consoantes)
#para criar uma tupla com um unico elemento precisa colocar uma virgula final

t=('elemento')
print(type(t))
tp=('elemento',)
print(type(tp))
#tupla vazia
t=tuple()
print(t)
#tupla com elementos de sequencia
t=tuple("cidade")
print(t)

cidades = ["Curitiba", "Recife", "Fortaleza", "Salvador", "Manaus", "Belém", "Florianópolis", "Goiânia", "Cuiabá", "Natal"]

tupla_cidades=tuple(cidades)
print(tupla_cidades)

#operadores

print(tupla_cidades[0])
print(tupla_cidades[::-1])
print(tupla_cidades[0:3])
# se tentar mudar elemento da tupla recebera um ero
try:
    tupla_cidades[0]='Poá'
except:
    print('Tuplas sao imutaveis')

# voce pode subistituir uma tupla por outra

endereco_tupla_cidade=id(tupla_cidades)
print('endereco_tupla_cidade ',endereco_tupla_cidade)
print(tupla_cidades)
tupla_cidades=tupla_cidades+('Irece',)
novo_endereco_tupla_cidade=id(tupla_cidades)
print('novo_endereco_tupla_cidade ',novo_endereco_tupla_cidade)
print(tupla_cidades)
