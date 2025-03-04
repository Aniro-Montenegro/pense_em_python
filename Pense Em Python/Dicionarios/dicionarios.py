#Um dicionártion é uma estrutura de chaves e valores

dicionario={"chave":"valor"}
valor=dicionario["chave"]
# Acessando todas as chaves
for chave in dicionario.keys():
    print("Chave:", chave)

# Acessando todos os valores
for valor in dicionario.values():
    print("Valor:", valor)

# Acessando chaves e valores juntos
for chave, valor in dicionario.items():
    print("Chave:", chave, "| Valor:", valor)

dicionario_novo=dict()

#adicionando elementos no dicionario
dicionario_novo["novo_valor"]=10
print(dicionario_novo)

#dicionarios nao sao ordenados

#len no dicionario
tamanho=len(dicionario_novo)
print(tamanho)

# operador in relacionado as chaves
print("novo_valor" in dicionario_novo)
print("valorr" in dicionario_novo)
#para saber se algum valor aparece
print(10 in dicionario_novo.values())
print(20 in dicionario_novo.values())

dicionario_novo["Valor1"]=25

## método get
valor=dicionario_novo["Valor1"]
print(valor)
v1=dicionario_novo.get("Valor1",0)
v2=dicionario_novo.get("Valor10",0)