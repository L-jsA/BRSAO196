'''Esse código implementa uma cifra de César, que é um tipo simples de criptografia onde cada letra é 
substituída por outra deslocada um número fixo de posições no alfabeto.'''


def alfabetoDuplicado(alfabeto): # Define uma função chamada alfabetoDuplicado que recebe um parâmetro chamado alfabeto.
    alfabetoduplo = alfabeto + alfabeto # Cria uma nova string chamada alfabetoduplo, que é o alfabeto duplicado. Exemplo: "ABC" vira "ABCABC".
    return alfabetoduplo # Retorna a string duplicada.

def obterMensagem(): # Define uma função chamada obterMensagem.
    mensagem = input("Digite uma mensagem para criptografar: ") # Exibe uma mensagem ao usuário e lê a entrada do teclado, armazenando em mensagem.
    return mensagem # Retorna a mensagem digitada pelo usuário

def obterChaveCifra(): # Define a função obterChaveCifra.
    while True: # Inicia um loop infinito que só vai parar quando uma chave válida for digitada.
        try: # Tenta executar o código abaixo (tratamento de erro).
            chave = int(input("Digite a chave (número inteiro entre 1 a 25): ")) # Pede ao usuário para digitar a chave e tenta converter para inteiro com int().
            if 1 <= chave <= 25: # Verifica se a chave está no intervalo de 1 a 25
                return chave # Se for válida, retorna a chave e sai do loop
            else: # Se não estiver no intervalo, mostra um aviso.
                print("A chave deve estar entre 1 e 25.")
        except ValueError: # Se o valor digitado não for um número inteiro, mostra essa mensagem.
            print("Por favor, digite um número inteiro válido.")

def criptografarMensagem(mensagem, chave, alfabeto): # Define a função criptografarMensagem com três parâmetros: a mensagem, a chave e o alfabeto.
    mensagemCriptografada = "" # Cria uma variável que vai armazenar o texto criptografado.
    mensagemMaiuscula = mensagem.upper() # Converte toda a mensagem para letras maiúsculas (a cifra só trata letras maiúsculas).
    alfabeto = alfabetoDuplicado(alfabeto) # Duplica o alfabeto usando a função alfabetoDuplicado.

    for caractereAtual in mensagemMaiuscula: # Inicia um laço que percorre cada caractere da mensagem
        if caractereAtual in alfabeto[:26]: # Verifica se o caractere atual é uma letra (está entre os 26 primeiros caracteres do alfabeto).
            posicao = alfabeto.find(caractereAtual) # Acha a posição da letra no alfabeto duplicado.
            novaPosicao = posicao + chave # Soma a chave à posição para encontrar a nova letra criptografada.
            mensagemCriptografada += alfabeto[novaPosicao] # Adiciona essa nova letra à mensagem criptografada.
        else: # Se o caractere não for uma letra (como espaço, número ou pontuação), mantém ele como está.
            mensagemCriptografada += caractereAtual 

    return mensagemCriptografada # Retorna a mensagem criptografada no final.

# Programa principal
if __name__ == "__main__": # Essa linha verifica se o arquivo está sendo executado diretamente (e não importado).Garante que o código abaixo só será executado quando o script for rodado como principal.
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Define o alfabeto em letras maiúsculas (26 letras).
    mensagem = obterMensagem() # Chama a função para pedir a mensagem ao usuário.
    chave = obterChaveCifra() # Chama a função para pedir a chave de criptografia ao usuário.
    mensagemCriptografada = criptografarMensagem(mensagem, chave, alfabeto) # Criptografa a mensagem com a chave informada.

    print("Mensagem criptografada:", mensagemCriptografada) # Exibe a mensagem criptografada final na tela
