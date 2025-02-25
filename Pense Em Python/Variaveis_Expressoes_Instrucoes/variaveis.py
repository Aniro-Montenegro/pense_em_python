# Variáveis são nomes usados para representar valores.
# Em Python, uma variável é criada quando um valor é atribuído a ela pela primeira vez.
# A variável é um nome que se refere a um valor.
# O operador de atribuição, =, cria uma nova variável ou altera o valor de uma variável existente.

# Exemplo de variáveis
x = 5
y = "Hello, World!"

# Uma Instrução de atrubuição é uma instrução que cria uma nova variável ou altera o valor de uma variável existente.
# Exemplo de instrução de atribuição
x = 5
print(x)
x= 10
print(x)
# O valor de x é 5, mas depois é alterado para 10.

#Nomes de variáveis
# Uma variável pode ter um nome curto (como x e y) ou um nome mais descritivo (idade, nome, volume_total).
# Regras para nomes de variáveis:
# - Um nome de variável deve começar com uma letra ou o caractere de sublinhado
# - Um nome de variável não pode começar com um número
# - Um nome de variável pode conter letras, números e caracteres de sublinhado
# - Os nomes de variáveis são sensíveis a maiúsculas e minúsculas (idade, Idade e IDADE são três variáveis diferentes)

# Exemplo de nomes de variáveis
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Variáveis de saída
# A função print() é usada para imprimir variáveis.
# Exemplo de variáveis de saída
x = "awesome"
print("Python is " + x)

#Palavras reservadas
# As palavras reservadas são palavras-chave que têm um significado especial no Python.
# Não é possível usar uma palavra reservada como nome de variável, função ou nome de classe.
# Exemplo de palavras reservadas
import keyword
print(keyword.kwlist)
# A função keyword.kwlist() retorna uma lista de todas as palavras-chave do Python.

# Variáveis múltiplas
# Python permite que você atribua valores a várias variáveis em uma linha:
# Exemplo de variáveis múltiplas
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Expressões e Instruções
# Expressões são combinações de valores, variaveis e operadoes.
# Uma instrução é uma unidade de código que o interpretador Python pode executar.
# Exemplo de expressões e instruções
x = 5
y = 10
print(x + y)
# Neste exemplo, x + y é uma expressão e print(x + y) é uma instrução.

# ordem das Operações(PEMDAS)
# Python segue a regra PEMDAS:
# - Parênteses tem a prioridade mais alta e podem ser usados para forçar a ordem de avaliação de uma expressão.
# - Exponenciação tem a próxima prioridade mais alta.
# - Multiplicação e divisão têm a mesma prioridade, que é maior que a adição e subtração, que também têm a mesma prioridade.
# - Operadores com a mesma prioridade são avaliados da esquerda para a direita.
# Exemplo de ordem das operações
x = 10 + 3 * 2
print(x)
# Neste exemplo, 3 * 2 é calculado primeiro
# e o resultado é adicionado a 10.
