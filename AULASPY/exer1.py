# DADOS MUTÁVEIS

lista = [1,2,3]
lista.append(4) #Adiciona o número 4 a lista anterior
print(lista)


texto = "Olá, mundo"
novo_texto = texto.replace("O", "A")
print(texto)
print (novo_texto)

# DADOS IMUTÁVEIS

'''texto2 = "45"
print(texto2 + 10) # Isso não será possível, pois não tem como juntar string mais inteiro'''

texto3 = "45"
numero = int(texto3) # Para alterar o tipo de dado, é necessário converter a string em um inteiro
print(numero + 10)