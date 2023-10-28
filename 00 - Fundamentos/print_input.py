###### função input #######
# exibe a mensagem, e ele espera a entrada, o retorno da variável input salva em nome.
nome = input("Informe o seu nome: ")

idade = input("Informe a sua idade: ")

# exibindo o valor com a função print
# por padrão o separador é o espaço em branco e a quebra de linha. 
# exibe o nome e o sobrenome
print(nome, idade)
# termina em tres pontos e faz uma quebra de linha
print(nome, idade, end="...\n")
# aqui adiciona o separador #
print(nome, idade, sep="#", end="...\n")

print(nome, idade, sep=" #")
