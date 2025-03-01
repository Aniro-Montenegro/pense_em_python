#divisao convencional
valor=77
divisao=valor/2
print(divisao,type(divisao))

#divisao pelo piso
minutes=10
horas=minutes//60
print("divisao pelo piso",horas, type(horas))

# operador modulo
minutos=177
resto=minutos%60
print(resto)

def minutos_horas(minutos):
    horas = minutos // 60
    min = minutos % 60
    minf = "{:02d}".format(min)  
    print(f"{horas}:{minf}")


minutos_horas(25)
minutos_horas(45)
minutos_horas(61)
minutos_horas(147)