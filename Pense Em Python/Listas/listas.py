lista_nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]
lista_nomes2 = ["Laura", "Marcos", "Natalia", "Otávio", "Patricia"]

print(lista_nomes)
print(lista_nomes[0])
lista_nomes[0]="Josue"
print(lista_nomes[0])

lista_numeros = [5, 12, 18, 23, 29, 34, 41, 47, 53, 60]

concateanacao=lista_nomes+lista_numeros
print(concateanacao)
print(lista_nomes[-1:])
print(lista_nomes[:-1])
print(lista_nomes[1:3])
print(lista_nomes[::-1])
print(lista_nomes[::-2])
concateanacao[2:4]=[45,45]
print(concateanacao)

##metodos listas
#adicionar elemnto
lista_nomes.append("Novo Nome")
print(lista_nomes)
lista_nomes.insert(0,"Primeira Posicao")
print(lista_nomes)
#extend toma uma lista e adiciona todos os elementos
lista_nomes.extend(lista_nomes2)
print("lista nomes ",lista_nomes)
print("lista nomes2 ",lista_nomes2)
# sort classifica os elemntos em ordem ascendente
lista_nomes.sort()
print(lista_nomes)
#pode-se ordenar de forma reversa
lista_nomes.sort(reverse=True)
print(lista_nomes)

## nova lista a partir de outra
nova_lista=lista_nomes2
lista_nomes2.append("Nome inserido na lista 2")
print(nova_lista)
print(lista_nomes2)

# Esse comportamento acontece porque, em Python, quando você faz uma atribuição como 
# nova_lista = lista_nomes2, você não está criando uma cópia da lista, mas sim fazendo 
# com que nova_lista aponte para o mesmo objeto na memória que lista_nomes2. Ou seja, 
# nova_lista e lista_nomes2 são duas referências para a mesma lista.
# Por isso, quando você modifica uma das listas (por exemplo, adicionando um item com append),
# a alteração é refletida em ambas as variáveis, pois elas estão apontando para o mesmo objeto.

lista_copia=lista_nomes2.copy()
lista_nomes2.append("Outro nome")
print(lista_copia)
print(lista_nomes2)
# O método .copy()  cria uma cópia independente da lista lista_nomes2. 
# Isso significa que lista_copia e lista_nomes2 são duas listas diferentes,
# e alterações em uma não afetam a outra.

# deletar elementos

#excluir elemnto por indice
elemento_deletado=lista_numeros.pop(0)
print(lista_numeros)
print(elemento_deletado)
lista_numeros.pop(0)
print(lista_numeros)
# se nao colocar um indice ele deleta o ultimo elemento
lista_numeros.pop()
print(lista_numeros)
lista_numeros.pop(-2)
print(lista_numeros)

#remove deleta o elemnto indicado
elemento_deletado=lista_numeros.remove(29)
print(lista_numeros)

#pare remover mais de um elemento use del
del lista_numeros[:2]
print(lista_numeros)
