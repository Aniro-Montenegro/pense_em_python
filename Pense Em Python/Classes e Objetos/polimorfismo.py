def calcular_gastos(*args):
    if len(args) == 1 and isinstance(args[0], list):
        # Se o argumento for uma lista de valores, soma todos os valores
        return sum(args[0])
    elif len(args) == 2 and isinstance(args[0], (int, float)) and isinstance(args[1], int):
        # Se forem dois argumentos (valor fixo e quantidade), multiplica-os
        return args[0] * args[1]
    else:
        raise ValueError("Argumentos inválidos. Esperado: lista de valores ou valor fixo e quantidade.")

# Exemplo de uso com uma lista de valores
gastos_lista = [10.5, 20.3, 30.2, 15.7]
total_lista = calcular_gastos(gastos_lista)
print(f"Total de gastos (lista): {total_lista}")

# Exemplo de uso com valor fixo e quantidade
valor_fixo = 25.0
quantidade = 4
total_fixo = calcular_gastos(valor_fixo, quantidade)
print(f"Total de gastos (valor fixo): {total_fixo}")



