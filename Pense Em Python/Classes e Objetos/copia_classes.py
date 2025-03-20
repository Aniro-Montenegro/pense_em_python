
import copy

class Marca:
    def __init__(self,marca):
        self.marca=marca
class Operacoes:
    def __init__(self,carro,km,litros_km,marca):
        self.carro=carro
        self.km=km
        self.litros_km=litros_km
        self.marca=Marca(marca)

    def nome_marca(self):
        print(f"Nome: {self.carro}, marca: {self.marca.marca}")
    
    def custo(self):
        return self.km*self.litros_km
    


# Criando instâncias de Operacoes com Marca
carro1 = Operacoes("Fiat Uno", 1000, 0.1, "Fiat")  # Fiat Uno, 1000 km, 10 litros por km, marca Fiat
carro2 = Operacoes("Volkswagen Gol", 1500, 0.12, "Volkswagen")  # Volkswagen Gol, 1500 km, 12 litros por km, marca Volkswagen
carro3 = Operacoes("Chevrolet Onix", 2000, 0.09, "Chevrolet")  # Chevrolet Onix, 2000 km, 9 litros por km, marca Chevrolet
carro4 = Operacoes("Ford Ka", 1200, 0.11, "Ford")  # Ford Ka, 1200 km, 11 litros por km, marca Ford
carro5 = Operacoes("Hyundai HB20", 1800, 0.1, "Hyundai")  # Hyundai HB20, 1800 km, 10 litros por km, marca Hyundai

# Exibindo informações
carros = [carro1, carro2, carro3, carro4, carro5]

for carro in carros:
    carro.nome_marca()
    print(f"Custo total: R${carro.custo():.2f}\n")


copia=copy.copy(carro1)
print(f"Carro 1: R${carro1.custo():.2f}\n")
print(f"Cópia do carro 1: R${copia.custo():.2f}\n")

# verificando se sao a mesma classe
print(copia is carro1)
print(copia == carro1)
print(copia.carro == carro1.carro)
id_copia=id(copia)
id_carro1=id(carro1)
id_carro_copia=id(copia.carro)
id_carro_carro1=id(carro1.carro)
id_marca=id(carro.marca)
id_marca_copy=id(copia.marca)
print(f"id_copia:{id_copia},id_carro1:{id_carro1},id_carro_copia:{id_carro_copia},id_carro1:{id_carro_carro1}, id_marca:{id_marca}, id_marca_copy:{id_marca_copy}  \n")
copia=copy.deepcopy(carro1)
id_copia=id(copia)
id_carro1=id(carro1)
id_carro_copia=id(copia.carro)
id_carro_carro1=id(carro1.carro)
print(f"id_copia:{id_copia},id_carro1:{id_carro1},id_carro_copia:{id_carro_copia},id_carro1:{id_carro_carro1}, id_marca:{id_marca}, id_marca_copy:{id_marca_copy}  ")