# import random

# def maior(a,b):
#     if a>b:
#         return f"O numero {a} é maior que {b}"
#     elif b>a:
#         return f"O numero {b} é maior que {a}"
#     else:
#         return f"Os numeros {a} e {b} são iguais"

# resultado=maior(10,5)
# # print(resultado)


# lista_numeros=[]
# for i in range(30):
#     lista_numeros.append(random.randrange(random.randrange(0,100),random.randrange(100,1000)))

# def busca_maior(lista):
#     print(lista)
#     maior=lista[0]
#     for a in lista:
#         if a>=maior:
#              maior=a
#     return maior

# print(busca_maior(lista_numeros))

# def fatorial(n):
#     if n==0:
#         return 1
#     else:
#         recurse=fatorial(n-1)
#         result=n*recurse
#         return result

# print(fatorial(4))
# def a(s,t):
#     s=s+1
#     return s*t
# def b(z):
#     prod=a(z,z)
#     print(z,prod)
#     return prod

# def c(x,y,z):
#     total=x+y+z
#     square=(b(total)**2)
#     return square

# h=1
# l=h+1
# print(c(h,l+3,h+l))


def mdc(a,b):
    if a%b==0:
        return b
    if b%a==0:
        return a
    if a==b:
        return a
    maior =1
    if a>b:
        maior=a
    else:
        maior=b
    ind=1
    mdc=1
    while(ind<maior):
        if a%ind==0 and b%ind==0:
            mdc=ind
        ind+=1
    return mdc

print(mdc(260,300))
