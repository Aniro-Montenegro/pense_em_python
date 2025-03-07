import string
caminho="Estudos_de_caso/criptografia.txt"
    

def abrir_arquivo(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
          conteudo = arquivo.read()          
          pontuacao= string.punctuation
          pontuacao=pontuacao+".[]()0123456789*-_""''"
          conteudo=conteudo.replace("."," ")
          for p in pontuacao:
               conteudo=conteudo.replace(p," ")
          conteudo=conteudo.replace("\n"," ")  
          lista=conteudo.split(" ")
          nova_lista=[]
          for i , a in enumerate(lista):
               if a!="" and a!=" ":                    
                    nova_lista.append(a)
               
          return nova_lista
          

def frequencia(lista):
     frequencia=dict()
     maior_tamanho=0
     for palavra in lista:
          if len(palavra)>maior_tamanho:
               maior_tamanho=len(palavra)
          if palavra not in frequencia:
               frequencia[palavra]=1
          else:
               frequencia[palavra]+=1
     frequencia_ordenada = sorted(frequencia.items(), key=lambda item: item[1],reverse=True)
     texto=''
     arquivo=open('Estudos_de_caso/frequencia_palavras.txt','w',encoding="utf-8")
     for c , v in frequencia_ordenada:
          texto=texto+ c+(((maior_tamanho-len(c))*" "))+" : "+str(v)+"\n"
          
     arquivo.write(texto)   
     arquivo.close()
          

lista_palavras=abrir_arquivo(caminho)

frequencia(lista_palavras)