caminho="Dicionarios/arquivo.txt"
    

def abrir_arquivo(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
          conteudo = arquivo.read()
          linhas=conteudo.split("`n")
          return linhas
    
arquivo=abrir_arquivo(caminho)
texto="".join(arquivo)
print(texto)

def contagem_caracteres(texto):
     dicionario_caracteres=dict()
     texto=texto.replace(" ", "").replace('', "").replace("\n", "")
     for c in texto:
          if c not in dicionario_caracteres:
               dicionario_caracteres[c]=1
          else:
               dicionario_caracteres[c]+=1
     for c in sorted(dicionario_caracteres):
          print(c,":",dicionario_caracteres[c])


contagem_caracteres(texto)