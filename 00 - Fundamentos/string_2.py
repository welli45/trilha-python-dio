
nome = "Wellington"
idade = 27
profissao = "Analista de dados"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Wellington", "idade": 28}
# old style %
# s -> string
# d -> inteiros
# f -> pontos flutuantes
# aqui as variáveis tem que está em ordem
print("Nome: %s Idade: %d" % (nome, idade))
# método format
# aqui tem colocar as variáveis em ordem
print("Nome: {} Idade: {}".format(nome, idade))
# podemos colocar nas chaves a ordem das variáveis - o indice que ela oculpa no format.
print("Nome: {1} Idade: {0}".format(idade, nome))
#  o uso do indice para repetir várias vezes o valor da variável
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))
#  nomeado voce pode passar em qualquer ordem.
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))
# f-tring
# coloca o f no inicio e dentro das chaves os nomes das variáveis.
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")
