# strings sao sequencias
linguagem="Python"
primeiro_caracter=linguagem[0]
print(primeiro_caracter)
frase="Mateus preocupa-se em apresentar a genealogia de Jesus, desde Abraão até Davi, mostrando Sua descendência real. Além disso, também descreve os acontecimentos do Seu nascimento, vida e morte. Diversos eventos são mencionados ao longo do livro, tais como: o início da vida de Jesus, Seu batismo feito por João Batista, o começo do Seu ministério, Suas pregações, como o Sermão da Montanha, as curas, como a cura de um leproso, até chegar aos últimos dias de ministério de Jesus, Sua morte e ressureição."

def contagem_caracter(caracter):
    contagem=0
    for a in frase:
        if a==caracter:
            contagem+=1
    return contagem

print(contagem_caracter('e'))

def ultima_letra(palavra):
    return palavra[-1]
print(ultima_letra('apresentar'))

print(frase[::-1])## invertendo string

# Exemplo de string
texto = "  Olá, Mundo!  "

# 1. str.capitalize() - Retorna a string com a primeira letra maiúscula.
print(texto.capitalize())  # Saída: "  olá, mundo!  "

# 2. str.casefold() - Retorna a string em minúsculas (mais agressivo que lower).
print(texto.casefold())  # Saída: "  olá, mundo!  "

# 3. str.center(width[, fillchar]) - Centraliza a string em um campo de largura especificada.
print(texto.center(20, '-'))  # Saída: "--  Olá, Mundo!  --"

# 4. str.count(sub[, start[, end]]) - Conta quantas vezes uma substring aparece na string.
print(texto.count('o'))  # Saída: 2

# 5. str.encode(encoding='utf-8', errors='strict') - Codifica a string em bytes.
print(texto.encode())  # Saída: b'  Ol\xc3\xa1, Mundo!  '

# 6. str.endswith(suffix[, start[, end]]) - Verifica se a string termina com um sufixo.
print(texto.endswith('!'))  # Saída: True

# 7. str.expandtabs(tabsize=8) - Substitui tabulações por espaços.
texto_tab = "Olá\tMundo!"
print(texto_tab.expandtabs(4))  # Saída: "Olá  Mundo!"

# 8. str.find(sub[, start[, end]]) - Retorna o índice da primeira ocorrência de uma substring.
print(texto.find('Mundo'))  # Saída: 7

# 9. str.format(*args, **kwargs) - Formata a string.
print("Olá, {}!".format("Mundo"))  # Saída: "Olá, Mundo!"

# 10. str.format_map(mapping) - Similar a format, mas usa um dicionário.
print("Olá, {nome}!".format_map({"nome": "Mundo"}))  # Saída: "Olá, Mundo!"

# 11. str.index(sub[, start[, end]]) - Retorna o índice da primeira ocorrência de uma substring (lança erro se não encontrar).
print(texto.index('Mundo'))  # Saída: 7

# 12. str.isalnum() - Verifica se todos os caracteres são alfanuméricos.
print("abc123".isalnum())  # Saída: True

# 13. str.isalpha() - Verifica se todos os caracteres são letras.
print("abc".isalpha())  # Saída: True

# 14. str.isascii() - Verifica se todos os caracteres são ASCII.
print("abc".isascii())  # Saída: True

# 15. str.isdecimal() - Verifica se todos os caracteres são decimais.
print("123".isdecimal())  # Saída: True

# 16. str.isdigit() - Verifica se todos os caracteres são dígitos.
print("123".isdigit())  # Saída: True

# 17. str.isidentifier() - Verifica se a string é um identificador válido.
print("var_name".isidentifier())  # Saída: True

# 18. str.islower() - Verifica se todos os caracteres são minúsculos.
print("olá".islower())  # Saída: True

# 19. str.isnumeric() - Verifica se todos os caracteres são numéricos.
print("123".isnumeric())  # Saída: True

# 20. str.isprintable() - Verifica se todos os caracteres são imprimíveis.
print("Olá!".isprintable())  # Saída: True

# 21. str.isspace() - Verifica se todos os caracteres são espaços.
print("   ".isspace())  # Saída: True

# 22. str.istitle() - Verifica se a string é um título (primeira letra de cada palavra maiúscula).
print("Olá Mundo".istitle())  # Saída: True

# 23. str.isupper() - Verifica se todos os caracteres são maiúsculos.
print("OLÁ".isupper())  # Saída: True

# 24. str.join(iterable) - Junta elementos de um iterável com a string como separador.
print(", ".join(["a", "b", "c"]))  # Saída: "a, b, c"

# 25. str.ljust(width[, fillchar]) - Justifica a string à esquerda.
print(texto.ljust(20, '-'))  # Saída: "  Olá, Mundo!  ----"

# 26. str.lower() - Converte a string para minúsculas.
print(texto.lower())  # Saída: "  olá, mundo!  "

# 27. str.lstrip([chars]) - Remove espaços à esquerda (ou caracteres especificados).
print(texto.lstrip())  # Saída: "Olá, Mundo!  "

# 28. str.maketrans(x[, y[, z]]) - Cria uma tabela de tradução para str.translate.
tabela = str.maketrans("áéíóú", "aeiou")
print("olá".translate(tabela))  # Saída: "ola"

# 29. str.partition(sep) - Divide a string em três partes usando o separador.
print(texto.partition(','))  # Saída: ('  Olá', ',', ' Mundo!  ')

# 30. str.replace(old, new[, count]) - Substitui uma substring por outra.
print(texto.replace('Mundo', 'Python'))  # Saída: "  Olá, Python!  "

# 31. str.rfind(sub[, start[, end]]) - Retorna o índice da última ocorrência de uma substring.
print(texto.rfind('o'))  # Saída: 11

# 32. str.rindex(sub[, start[, end]]) - Retorna o índice da última ocorrência de uma substring (lança erro se não encontrar).
print(texto.rindex('o'))  # Saída: 11

# 33. str.rjust(width[, fillchar]) - Justifica a string à direita.
print(texto.rjust(20, '-'))  # Saída: "----  Olá, Mundo!  "

# 34. str.rpartition(sep) - Divide a string em três partes usando o separador, começando pela direita.
print(texto.rpartition(' '))  # Saída: ('  Olá, Mundo!', ' ', '')

# 35. str.rsplit([sep[, maxsplit]]) - Divide a string em uma lista, começando pela direita.
print(texto.rsplit())  # Saída: ['Olá,', 'Mundo!']

# 36. str.rstrip([chars]) - Remove espaços à direita (ou caracteres especificados).
print(texto.rstrip())  # Saída: "  Olá, Mundo!"

# 37. str.split([sep[, maxsplit]]) - Divide a string em uma lista.
print(texto.split())  # Saída: ['Olá,', 'Mundo!']

# 38. str.splitlines([keepends]) - Divide a string em uma lista de linhas.
print("Olá\nMundo".splitlines())  # Saída: ['Olá', 'Mundo']

# 39. str.startswith(prefix[, start[, end]]) - Verifica se a string começa com um prefixo.
print(texto.startswith('  Olá'))  # Saída: True

# 40. str.strip([chars]) - Remove espaços (ou caracteres especificados) do início e do fim.
print(texto.strip())  # Saída: "Olá, Mundo!"

# 41. str.swapcase() - Inverte maiúsculas e minúsculas.
print("Olá Mundo".swapcase())  # Saída: "oLÁ mUNDO"

# 42. str.title() - Converte a string para formato de título.
print("olá mundo".title())  # Saída: "Olá Mundo"

# 43. str.translate(table) - Traduz a string usando uma tabela de tradução.
tabela = str.maketrans("áéíóú", "aeiou")
print("olá".translate(tabela))  # Saída: "ola"

# 44. str.upper() - Converte a string para maiúsculas.
print(texto.upper())  # Saída: "  OLÁ, MUNDO!  "

# 45. str.zfill(width) - Preenche a string com zeros à esquerda até atingir a largura especificada.
print("42".zfill(5))  # Saída: "00042"