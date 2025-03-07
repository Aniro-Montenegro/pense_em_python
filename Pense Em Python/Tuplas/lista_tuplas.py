carros = ["Gol", "Onix", "Civic", "Corolla", "Fiesta", "Hilux", "Cruze", "Uno", "Polo", "Renegade"]
valores=[100000,200000,30000]
# se nao tiverem o mesmo comprimento, o resultado tera o tamanho da mais curta

valores_carros=zip(valores,carros)
lista_desempacotada = list(valores_carros)  # Converte para uma lista
print(lista_desempacotada)
valores_carros=zip(valores,carros)
for vc in valores_carros:
    print(vc)



