# String e fatiamento
# O modo de uso é mais ambrangente.

# Maiúsculo 
nome = "gUIlherME"

# converte para maiúsculo
print(nome.upper())
# converte para minúsculo
print(nome.lower())
# converte a primeira Letra para maiúsculo
print(nome.title())

texto = "  Olá mundo!    "
# o ponto final é só para verificar!
print(texto + ".")
# remove o espaço em branco no início e no final
print(texto.strip() + ".")
# removo do lado direito
print(texto.rstrip() + ".")
# remove da esquerdo
print(texto.lstrip() + ".")

menu = "Python"
# a forma como queremos que o texto apareça
print("####" + menu + "####")
# Centralida a string e adiciona uma quantidade de caracter no final e no início da string
print(menu.center(14))
# aqui definimos o valor do inicio e final
print(menu.center(14, "#"))
# passa por cada item e adiciona um traço entre as letras
print("-".join(menu))
