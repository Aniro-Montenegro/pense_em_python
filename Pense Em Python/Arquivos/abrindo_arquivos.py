novo_arquivo= open('//Volumes/ANIRO_IOS/Estudos Python/pense_python_livro/pense_em_python/Pense Em Python/Arquivos/novo_arquivo.txt','w')

import random

# Lista de nomes próprios mais comuns no Brasil
nomes = [
    "Maria", "João", "Ana", "Pedro", "Marcos", "Juliana", "Carlos", "Fernanda", "Lucas", "Patrícia",
    "Gabriel", "Amanda", "Rafael", "Camila", "Rodrigo", "Beatriz", "Felipe", "Jéssica", "Gustavo", "Letícia"
]

# Lista de sobrenomes do meio mais comuns no Brasil
sobrenomes_meio = [
    "Silva", "Santos", "Oliveira", "Souza", "Pereira", "Lima", "Gomes", "Costa", "Ribeiro", "Martins",
    "Almeida", "Nunes", "Carvalho", "Mendes", "Barbosa", "Freitas", "Ferreira", "Vieira", "Rocha", "Monteiro"
]

# Lista de sobrenomes finais mais comuns no Brasil
sobrenomes_finais = [
    "Souza", "Silva", "Santos", "Oliveira", "Pereira", "Alves", "Lima", "Carvalho", "Melo", "Castro",
    "Fernandes", "Barros", "Freitas", "Ramos", "Gonçalves", "Borges", "Cavalcanti", "Duarte", "Teixeira", "Araújo"
]

# Gerar nomes aleatórios completos
nomes_completos = [f"{random.choice(nomes)} {random.choice(sobrenomes_meio)} {random.choice(sobrenomes_finais)}" for _ in range(30)]


for nome in nomes_completos:
    novo_arquivo.write(nome+'\n')

novo_arquivo = open('//Volumes/ANIRO_IOS/Estudos Python/pense_python_livro/pense_em_python/Pense Em Python/Arquivos/novo_arquivo.txt', 'a')
nome1=f"Nome Adicionado"
novo_arquivo.write(nome1)

novo_arquivo.close()