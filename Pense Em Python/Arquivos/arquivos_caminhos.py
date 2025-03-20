import os
cwd=os.getcwd()
print(cwd)

caminho_absoluto=os.path.abspath('valores_retorno.py')
print(caminho_absoluto)

lista_diretorios=os.listdir('/Volumes/')
print(lista_diretorios)

arquivo_diretorios=open('Arquivos/arquivo_diretrios.txt','w')


def percore(dirname):
  for name in os.listdir(dirname):
    path=os.path.join(dirname,name)
    if os.path.isfile(path):
      arquivo_diretorios.write(path+'\n')
    else:
      percore(path)

percore('/Volumes/ANIRO_IOS/Estudos Python/pense_python_livro/pense_em_python/Pense Em Python/Arquivos')