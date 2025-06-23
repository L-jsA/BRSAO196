#LIÇÃO NOVE - CONDICIONAIS
'''respostaUser = input ("Você precisa enviar um pacote? (Digite 'sim' ou 'não')")
print (respostaUser)

if respostaUser == "sim":
    print ("Podemos te ajudar a enviar o pacote")

else:
    print ("Volte quando precisar enviar um pacote. Obrigado!")'''

respostaUsuario = input("Você gostaria de comprar selos, comprar um envelope ou fazer uma cópia (Digite selos, envelope ou copia)? ") #faz uma pergunta ao usuário

if respostaUsuario == "selos": # se ele escolher "selos" aparece essa opção
    print("Temos muitos desingn de selos para escolher.")

elif respostaUsuario == "envelope": # se ele escolher "envelope" aparece essa opção
    print("Temos muitos tamanhos de envelopes para escolher.")

elif respostaUsuario == "copia": # se ele escolher "cópia aparece essa opção
    quantidade = input("Quantas cópias você gostaria (Digite um número)? ")
    print(f"Aqui estão suas {quantidade} cópias")

else: # se não escolher nenhuma das opções, aparece essa
    print("Obrigado, volte sempre.")
 