import dbm
import pickle
db=dbm.open('/Volumes/ANIRO_IOS/Estudos Python/pense_python_livro/pense_em_python/Pense Em Python/Arquivos/banco','c')

carros_mais_vendidos = [
    "Chevrolet Onix", "Hyundai HB20", "Volkswagen Polo", "Fiat Strada", "Fiat Mobi",
    "Chevrolet Tracker", "Toyota Corolla Cross", "Jeep Compass", "Volkswagen T-Cross", "Renault Kwid"
]
listas_de_placas = [
    ["ABC-1D23", "XYZ-2E45", "JKL-3F67", "MNO-4G89", "PQR-5H12", "STU-6I34", "VWX-7J56", "YZA-8K78", "BCD-9L90", "EFG-0M11"],
    ["HIJ-1N22", "KLM-2O33", "NOP-3P44", "QRS-4Q55", "TUV-5R66", "WXY-6S77", "ZAB-7T88", "CDE-8U99", "FGH-9V00", "IJK-0W11"],
    ["LMN-1X22", "OPQ-2Y33", "RST-3Z44", "UVW-4A55", "XYZ-5B66", "ABC-6C77", "DEF-7D88", "GHI-8E99", "JKL-9F00", "MNO-0G11"],
    ["PQR-1H22", "STU-2I33", "VWX-3J44", "YZA-4K55", "BCD-5L66", "EFG-6M77", "HIJ-7N88", "KLM-8O99", "NOP-9P00", "QRS-0Q11"],
    ["TUV-1R22", "WXY-2S33", "ZAB-3T44", "CDE-4U55", "FGH-5V66", "IJK-6W77", "LMN-7X88", "OPQ-8Y99", "RST-9Z00", "UVW-0A11"],
    ["XYZ-1B22", "ABC-2C33", "DEF-3D44", "GHI-4E55", "JKL-5F66", "MNO-6G77", "PQR-7H88", "STU-8I99", "VWX-9J00", "YZA-0K11"],
    ["BCD-1L22", "EFG-2M33", "HIJ-3N44", "KLM-4O55", "NOP-5P66", "QRS-6Q77", "TUV-7R88", "WXY-8S99", "ZAB-9T00", "CDE-0U11"],
    ["FGH-1V22", "IJK-2W33", "LMN-3X44", "OPQ-4Y55", "RST-5Z66", "UVW-6A77", "XYZ-7B88", "ABC-8C99", "DEF-9D00", "GHI-0E11"],
    ["JKL-1F22", "MNO-2G33", "PQR-3H44", "STU-4I55", "VWX-5J66", "YZA-6K77", "BCD-7L88", "EFG-8M99", "HIJ-9N00", "KLM-0O11"],
    ["NOP-1P22", "QRS-2Q33", "TUV-3R44", "WXY-4S55", "ZAB-5T66", "CDE-6U77", "FGH-7V88", "IJK-8W99", "LMN-9X00", "OPQ-0Y11"]
]

tabela_carros=dict()
tabela_carros[ "Chevrolet Onix"]=listas_de_placas[0]
for carro in carros_mais_vendidos:
    for c,v in enumerate(listas_de_placas):
        tabela_carros[carro]=v
        db[carro]=pickle.dumps(v)
   

for key in db.keys():
    print(key, pickle.loads(db[key]))
