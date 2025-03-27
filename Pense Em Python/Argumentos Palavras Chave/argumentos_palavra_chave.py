passaros = {
    "Sabiá-laranjeira": "Brasil",
    "Beija-flor": "Américas",
    "Tucano": "Brasil e América Central",
    "Arara-azul": "Brasil, Paraguai, Bolívia",
    "Pardal": "Europa e Ásia (introduzido globalmente)",
    "Quetzal": "México e América Central",
    "Pinguim-de-magalhães": "Argentina e Chile",
    "Águia-careca": "Estados Unidos e Canadá",
    "Kiwi": "Nova Zelândia",
    "Cegonha-branca": "Europa e África"
}

def printAll(*args, **kwargs):
    # Imprime argumentos posicionais
    print("Argumentos posicionais:")
    for arg in args:
        print(arg)
    
    # Imprime argumentos nomeados
    print("\nArgumentos nomeados:")
    for key, value in kwargs.items():
        print(f"{key}:")
        if isinstance(value, dict):  # Se o valor for um dicionário
            for subkey, subvalue in value.items():
                print(f"  {subkey}: {subvalue}")
        else:
            print(f"  {value}")

printAll(1, 2, 3, aves=passaros)

