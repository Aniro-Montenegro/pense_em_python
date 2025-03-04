carros = {
    "Fusca": 25000.00,
    "Civic": 120000.50,
    "Corolla": 150000.75,
    "HB20": 70000.00,
    "Onix": 80000.25,
    "Golf": 130000.90,
    "Jeep Compass": 200000.00,
    "Tesla Model S": 500000.99,
    "Porsche 911": 800000.50,
    "Ferrari F40": 1500000.00
}

for c in carros:
    print(c,":", carros[c])
print()
for c in sorted(carros):
    print(c,":", carros[c]) 


def busca_reversa(dicionario,valor):
    for k in dicionario:
        if dicionario[k]==valor:
            return {k:dicionario[k]}
    return {}

print(busca_reversa(carros,10))
print(busca_reversa(carros,1500000.00))