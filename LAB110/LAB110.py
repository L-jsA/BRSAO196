#LIÇÃO TRÊS - TIPOS DE DADOS DE STRING
mensagem = "Isso é uma string"
print (mensagem)
print (type(mensagem)) #mostra o tipo de dado (string)
print(str(mensagem) + " é do tipo de dado string" + str(type(mensagem))) #converte o dado para string e mostra o tipo de dado
print (f"{mensagem} é o tipo de dado {type(mensagem)}") # também converte o dado para string e mostra o tipo de dado (forma simplificada). As f-strings tornam o código mais limpo, legível e eficiente.

primeiroNome = "Luana"
segundoNome = "Andrade"
nomeCompleto = primeiroNome + segundoNome #concatena (junta) as palavras
print(nomeCompleto)

nome = input ("Qual é o seu nome?")
cor = input ("Qual sua cor favorita?")
animal = input ("Qual seu animal favorita?")
print ("{}, gosta da cor {}, e do animal {}".format(nome, cor, animal)) #Strings + variáveis
print (f"{nome}, gosta da cor {cor}, e do animal {animal}") # F-strings (a mesma coisa do print anterior)