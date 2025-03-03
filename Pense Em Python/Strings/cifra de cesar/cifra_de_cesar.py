# Abrir o arquivo em modo de leitura ('r')

caminho="Strings/cifra de cesar/arquivo.txt"
    

def abrir_arquivo(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
          conteudo = arquivo.read()
          linhas=conteudo.split("`n")
          return linhas


def cifragem(lista, chave):
     nova_lista=[]
     for l in lista:
          frase=l.split(" ")
          frase_nova=[]
          for f in frase:
               nova_palavra=""
               for cont, ch in enumerate(f):
                    ordn=ord(ch)
                    novo_caracter=chr(ordn+chave)
                    nova_palavra=nova_palavra+novo_caracter
                    nova_palavra=nova_palavra.replace("\n","")
               frase_nova.append(nova_palavra)
          nova_lista.append(", ".join(frase_nova))  
     return nova_lista
                         
      
def des_cifragem(lista, chave):
     nova_lista=[]
     for l in lista:
          frase=l.split(" ")
          frase_nova=[]
          for f in frase:
               nova_palavra=""
               for cont, ch in enumerate(f):                    
                    ordn=ord(ch)
                    novo_ordn=ordn-chave                    
                    novo_caracter=chr(novo_ordn)
                    nova_palavra=nova_palavra+novo_caracter
                    nova_palavra=nova_palavra.replace("\\n","")
               frase_nova.append(nova_palavra)
          
               
          nova_lista.append(",".join(frase_nova))  
     return nova_lista

listaTexto=abrir_arquivo(caminho)
texto_cifrado=cifragem(listaTexto,5)
print(texto_cifrado)
texto_descifrado=des_cifragem(texto_cifrado,5)
print(texto_descifrado)
texto_pronto=", ".join(texto_cifrado)

with open("Strings/cifra de cesar/novo_arquivo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(texto_pronto)
               

