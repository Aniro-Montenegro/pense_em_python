pessoas = {
    "João": {"sexo": "masculino", "idade": 25},
    "Maria": {"sexo": "feminino", "idade": 30},
    "Pedro": {"sexo": "masculino", "idade": 22},
    "Ana": {"sexo": "feminino", "idade": 28},
    "Carlos": {"sexo": "masculino", "idade": 35},
    "Laura": {"sexo": "feminino", "idade": 19},
    "Lucas": {"sexo": "masculino", "idade": 27},
    "Mariana": {"sexo": "feminino", "idade": 24},
    "Fernando": {"sexo": "masculino", "idade": 40},
    "Beatriz": {"sexo": "feminino", "idade": 31},
    "Rafael": {"sexo": "masculino", "idade": 29},
    "Juliana": {"sexo": "feminino", "idade": 26},
    "Gustavo": {"sexo": "masculino", "idade": 33},
    "Camila": {"sexo": "feminino", "idade": 23},
    "Daniel": {"sexo": "masculino", "idade": 38},
    "Amanda": {"sexo": "feminino", "idade": 20},
    "Marcos": {"sexo": "masculino", "idade": 45},
    "Isabela": {"sexo": "feminino", "idade": 32},
    "Roberto": {"sexo": "masculino", "idade": 50},
    "Patrícia": {"sexo": "feminino", "idade": 36},
    "Felipe": {"sexo": "masculino", "idade": 21},
    "Tatiane": {"sexo": "feminino", "idade": 29},
    "André": {"sexo": "masculino", "idade": 42},
    "Claudia": {"sexo": "feminino", "idade": 39},
    "Rodrigo": {"sexo": "masculino", "idade": 31},
    "Vanessa": {"sexo": "feminino", "idade": 27},
    "Eduardo": {"sexo": "masculino", "idade": 34},
    "Renata": {"sexo": "feminino", "idade": 25},
    "Antônio": {"sexo": "masculino", "idade": 48},
    "Bianca": {"sexo": "feminino", "idade": 22},
    "Márcio": {"sexo": "masculino", "idade": 37},
    "Letícia": {"sexo": "feminino", "idade": 24},
    "Vinícius": {"sexo": "masculino", "idade": 26},
    "Natália": {"sexo": "feminino", "idade": 30},
    "Sérgio": {"sexo": "masculino", "idade": 43},
    "Adriana": {"sexo": "feminino", "idade": 38},
    "Thiago": {"sexo": "masculino", "idade": 28},
    "Priscila": {"sexo": "feminino", "idade": 33},
    "Ricardo": {"sexo": "masculino", "idade": 52},
    "Monica": {"sexo": "feminino", "idade": 41},
    "Bruno": {"sexo": "masculino", "idade": 23},
    "Raquel": {"sexo": "feminino", "idade": 29},
    "Alexandre": {"sexo": "masculino", "idade": 46},
    "Cristina": {"sexo": "feminino", "idade": 35},
    "Diego": {"sexo": "masculino", "idade": 31},
    "Larissa": {"sexo": "feminino", "idade": 27},
    "Leonardo": {"sexo": "masculino", "idade": 39},
    "Aline": {"sexo": "feminino", "idade": 26},
    "José": {"sexo": "masculino", "idade": 55},
    "Tânia": {"sexo": "feminino", "idade": 44}
}
idade=65
lista=[(chave, pessoas[chave] )for chave in pessoas if pessoas[chave]["idade"]>=idade]
for l in lista:
    print(l)

lista_booleana = [pessoas[chave]["idade"] >= idade for chave in pessoas]
for l in lista_booleana:
    print(l)

print(f'Na lista tem alguem com idade igual ou maior que {idade}:',"sim" if any(lista_booleana) else "não")