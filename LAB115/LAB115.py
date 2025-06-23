#LIÇÃO DEZ - LOOPS FOR W WHILE

import random

print ("Bem-vindo ao jogo Adivinhe o número")
print ("As regras são simples: Eu vou pensar em um número e você tentará adivinhar")

number = random.randint(1, 10) #Gera um número aleatório entre 1 e 10 (inclusive).
isGuessRight = False #Cria uma variável booleana que controla o loop.

while isGuessRight != True: #Esse é o loop que continuará executando enquanto o usuário não acertar o número. Se for difernte de true (false) ele irá continuar no loop.
    guess = input ("Adivinhe o número de 1 a 10:") #Pede que o usuário digite um número
    if int (guess) == number: #Converte o valor digitado (guess) para int, e compara com o número sorteado.Se forem iguais, o jogador acertou.
        print (" Você digitou {}. Isso está correto! Você venceu." .format(guess)) #Exibe uma mensagem de vitória com o número digitado, usando .format() para inserir a variável guess.
        isGuessRight = True #Como o jogador acertou, define isGuessRight como True, encerrando o while.
    else: 
        print ("Você digitou {}. Desculpe, não é esse número. Tente outra vez" .format(guess)) #Se o número não for o correto, mostra uma mensagem de erro e o loop continua.