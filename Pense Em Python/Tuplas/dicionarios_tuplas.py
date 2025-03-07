#funcao items deveolve uma sequencia den tuplas

estados = {
    "SP": "São Paulo",
    "RJ": "Rio de Janeiro",
    "MG": "Minas Gerais",
    "BA": "Bahia",
    "PR": "Paraná",
    "RS": "Rio Grande do Sul",
    "PE": "Pernambuco",
    "CE": "Ceará",
    "PA": "Pará",
    "SC": "Santa Catarina"
}

print(estados)

estados_itens=estados.items()
print(estados_itens)
print(type(estados_itens))

for key ,value in estados_itens:
    print(key,":",value)


#caminho inverso

campeoes_brasileiros = [
    ("Palmeiras", 12),
    ("Santos", 8),
    ("Flamengo", 8),
    ("Corinthians", 7),
    ("São Paulo", 6),
    ("Cruzeiro", 4),
    ("Vasco", 4),
    ("Fluminense", 4),
    ("Internacional", 3),
    ("Grêmio", 3)
]

dicionario_campeoes=dict(campeoes_brasileiros)
print(dicionario_campeoes)
print(type(dicionario_campeoes))

#combinando dict com zip

cidades_turisticas = ["Paris", "Nova York", "Londres", "Tóquio", "Roma"]
notas=[8,7.5,9.6,7,8.3]
cidades_notas=dict(zip(cidades_turisticas,notas))
print(cidades_notas)


nomes = [
    ("Ana", "Silva"), ("Bruno", "Souza"), ("Carlos", "Pereira"), ("Daniela", "Oliveira"),
    ("Eduardo", "Santos"), ("Fernanda", "Lima"), ("Gabriel", "Ferreira"), ("Helena", "Costa"),
    ("Igor", "Martins"), ("Juliana", "Rodrigues"), ("Karen", "Almeida"), ("Lucas", "Mendes"),
    ("Mariana", "Barbosa"), ("Natália", "Carvalho"), ("Otávio", "Ramos"), ("Patrícia", "Gomes"),
    ("Rafael", "Teixeira"), ("Sara", "Vieira"), ("Tiago", "Moreira"), ("Vanessa", "Duarte")
]
telefones = [
    "11987654321", "21987654322", "31987654323", "41987654324", "51987654325",
    "61987654326", "71987654327", "81987654328", "91987654329", "11987654330",
    "21987654331", "31987654332", "41987654333", "51987654334", "61987654335",
    "71987654336", "81987654337", "91987654338", "11987654339", "21987654340"
]
nomes_telefone={}
i=0
while i<len(nomes):
    nomes_telefone[nomes[i]]=telefones[i]
    i+=1

print(nomes_telefone)

for last,first in nomes_telefone:
    print(last,first,nomes_telefone[last,first])

## sorted e reversed
lista_telefones_ordenada=sorted(telefones)
print(lista_telefones_ordenada)
lista_telefones_ordenada_reverse=reversed(telefones)
for i in lista_telefones_ordenada_reverse:
    print(i)