
def resto_divisao(a,b):
    print(a//b)



t=(11,7)

try:
    resto_divisao((11,7))
except:
    print("Não é possivel fazer essa atribuicao")

resto_divisao(*t)