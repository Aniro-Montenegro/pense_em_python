import string
import random

def abrir_arquivo(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
          conteudo = arquivo.read()          
          pontuacao= string.punctuation
          pontuacao='!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~[]()0123456789*-_""'
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


caminho="Estudos_de_caso/criptografia.txt"
lista=abrir_arquivo(caminho)

dicionario=dict()

i=0
while i<len(lista)-1:
     if lista[i] not in dicionario:
          dicionario[lista[i]]=[lista[i+1]]
     else:
          dicionario[lista[i]].append(lista[i+1])        
     
     i+=1


def criar_texto_aleatorio(dicionario,palavra,quantidade):
     contagem_palavras=0
     i=0
     texto=''
     texto=texto+palavra
     while i<quantidade:
          for chave, valor in dicionario.items():            
               if chave==palavra and contagem_palavras!=15:
                    texto=texto+" "+valor[random.randint(0,len(valor)-1)]
                    palavra=valor[0]                          
                    contagem_palavras+=1
               elif chave==palavra :
                    texto=texto+"\n"+valor[random.randint(0,len(valor)-1)]
                    palavra=valor[0]                          
                    contagem_palavras=0

           
               
          
                    
                
          i+=1
         
     return texto


texto=criar_texto_aleatorio(dicionario,'Criptografia',20)
arquivo=open('Estudos_de_caso/markov.txt','w',encoding="utf-8")
arquivo.write(texto)
arquivo.close()


          
          