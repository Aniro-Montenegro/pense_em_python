import turtle
def quadrado(lado):
    qrd=turtle.Turtle()
    
    for i in range(4):
        qrd.fd(lado)
        qrd.lt(90)
    turtle.mainloop()

"""
Funcao que desenha um poligono
"""
def poligono(lados,tamanho):
    qrd=turtle.Turtle()
    for i in range(lados):
        qrd.fd(tamanho)
        qrd.lt(360/lados)
    turtle.mainloop()


# poligono(50,10)
