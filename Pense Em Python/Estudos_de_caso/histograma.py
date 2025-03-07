
caminho="Estudos_de_caso/criptografia.txt"

import frequencia 


def probabilidade(lista):
    tamanho = len(lista)
    dicionario = {}
    maior_tamanho=0
    for a in lista:
        if len(a)>maior_tamanho:
               maior_tamanho=len(a)
        if a not in dicionario:
            dicionario[a] = 1
        else:
            dicionario[a] += 1
    frequencia_ordenada = sorted(dicionario.items(), key=lambda item: item[1], reverse=True)
  
    dicionario_prob = {chave: "{:.2f}".format((valor / tamanho) * 100) for chave, valor in frequencia_ordenada}
    arquivo=open('Estudos_de_caso/porcentagem.txt','w',encoding="utf-8")
    texto=''
    for c , v in dicionario_prob.items():
          texto=texto+ c+(((maior_tamanho-len(c))*" "))+" : "+str(v)+"\n"
          
    arquivo.write(texto)   
    arquivo.close()

   

    
lista_palavras=frequencia.abrir_arquivo(caminho)

lista_frequencia=probabilidade(lista_palavras)
