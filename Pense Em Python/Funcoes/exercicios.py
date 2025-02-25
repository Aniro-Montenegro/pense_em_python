#criar uma funcao que recebe uma string e que ao imprimir garante que o ultimo caracter esteja na posicao 70
def right_justify(palavra):
    tamanho_palavra=len(palavra)
    palavra=(" "*(70-tamanho_palavra))+palavra
    print(palavra)

right_justify("Esperanca")
right_justify("Paralelepipido")
right_justify("Oi")


# print grade

def printGrade(repeticao,colunas):
    base=(("+"+("-"*(repeticao+1)))*(colunas-1))+"+"
    coluna=("|"+(" "*(repeticao+1))) *(colunas-1)+"|"
    for x in range(repeticao-1):
        print(base)
        for z in range(repeticao):
            print(coluna)
    print(base)
    


printGrade(10,10)