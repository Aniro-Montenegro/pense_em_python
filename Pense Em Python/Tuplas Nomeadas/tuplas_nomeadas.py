import random
from collections import namedtuple

Pessoa = namedtuple('Pessoa', ['nome', 'idade'])

# Listas de nomes e sobrenomes
nomes_masculinos = ["Miguel", "Arthur", "Heitor", "Gael", "Davi", "Bernardo", "Gabriel", "Lorenzo", "Pedro", "Theo"]
nomes_femininos = ["Sophia", "Alice", "Julia", "Isabella", "Helena", "Valentina", "Laura", "Maria Eduarda", "Giovanna", "Manuela"]
sobrenomes_brasil = [
    "Silva", "Santos", "Oliveira", "Souza", "Rodrigues", 
    "Ferreira", "Alves", "Pereira", "Lima", "Gomes",
    "Costa", "Ribeiro", "Martins", "Carvalho", "Araújo",
    "Melo", "Barbosa", "Monteiro", "Almeida", "Nascimento"
]

# Criando pessoas adultas
pessoas = []
for _ in range(20):
    nome = f"{random.choice(nomes_masculinos)} {random.choice(sobrenomes_brasil)}"
    pessoas.append(Pessoa(nome, random.randint(18, 75)))
    
    nome = f"{random.choice(nomes_femininos)} {random.choice(sobrenomes_brasil)}"
    pessoas.append(Pessoa(nome, random.randint(18, 75)))

print("Adultos:")
for p in pessoas:
    print(p.nome, p.idade)

# Classe para crianças
class Crianca(Pessoa):
    def __new__(cls, nome, idade, escolar):
        self = super().__new__(cls, nome, idade)
        self.escolar = escolar
        return self

# Criando crianças
criancas = []
for i in range(20):
    escolar = i % 2 == 0  # Alterna entre True e False
    nome = f"{random.choice(nomes_masculinos)} {random.choice(sobrenomes_brasil)}"
    criancas.append(Crianca(nome, random.randint(1, 17), escolar))
    
    escolar = not escolar
    nome = f"{random.choice(nomes_femininos)} {random.choice(sobrenomes_brasil)}"
    criancas.append(Crianca(nome, random.randint(1, 17), escolar))

print("\nCrianças:")
for c in criancas:
    print(c.nome, c.idade, c.escolar)