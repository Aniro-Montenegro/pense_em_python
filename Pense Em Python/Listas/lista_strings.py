# strings em listas
s='banana'
lista=list(s)
print(lista)
versiculo="Eu os conduzi com laços de bondade humana e de amor; tirei do seu pescoço o jugo e me inclinei para alimentá-los."
lista_versiculo=versiculo.split()
print(lista_versiculo)
# delimiter
lista_delimiter=versiculo.split(";")
print(lista_delimiter)

# join concatena uma lista em string, deve-se usar um delimitador
lista_versiculo=versiculo.split()
delimiter=" "
versiculo_join=delimiter.join(lista_versiculo)
print(versiculo_join)