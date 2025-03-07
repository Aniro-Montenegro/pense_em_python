#para trocar valores entre variaveis precisamos de uma variavel temporaria

a=10
b=5
print(a,b)
temp=a
a=b
b=temp
print(a,b)
#atribuicao de tuplas
a=10
b=5
print(a,b)
a,b=b,a
print(a,b)

dados="Jesse-458965"
nome,rg=dados.split("-")
print(nome,rg)
print(type(nome))