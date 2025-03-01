import time
import random
tempo=time.time()
minutos =tempo//60
horas =minutos//60
dias=horas//24
anos=dias//365
print(tempo,minutos, horas, dias, anos)


def check_fermat(a,b,c,n):
    return (a**n)+(b**n)==c**n



# for a in range(250):
#     print(check_fermat(random.randint(2, 500000) ,random.randint(2, 50000),random.randint(2, 500000),random.randint(2, 1000)),a)


def is_triangle(a,b,c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return "Yes"
    else:
        return "No"
    

for x in range(10):
    a=random.randint(10, 50)
    b=random.randint(10, 50)
    c=random.randint(10, 50)
    print(is_triangle( a,b,c),a,b,c)