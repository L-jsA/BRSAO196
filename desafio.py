'''Seu Desafio

Escreva um script Python para:

Exiba todos os números primos entre 1 e 250.
Armazene os resultados em um arquivo results.txt.
Teste o script. Verifique se ele produziu os resultados esperados no arquivo results.txt.
Salve o script e anote sua localização (caminho absoluto) para referência futura.
'''

def eh_primo(numero): # Define uma função chamada eh_primo que recebe um argumento numero. O objetivo da função é verificar se o número é primo (ou seja, divisível apenas por 1 e por ele mesmo).
    if numero <= 1: # Se o número for menor ou igual a 1, a função retorna False, pois números menores que 2 não são primos.
        return False
    # Este for verifica todos os números i de 2 até a raiz quadrada de numero, arredondada para baixo (com int(...)), somando 1 para incluir o limite.
    # Isso é feito porque, se numero for divisível por algum número além da raiz quadrada, ele também seria divisível por algum número menor do que ela. Então essa é uma forma eficiente de verificar primalidade.
    for i in range(2, int(numero**0.5) + 1):
      if numero % i == 0: # Se o número for divisível por i, então ele não é primo, e a função retorna False imediatamente.
          return False
    return True # Se o loop termina sem encontrar nenhum divisor, o número é primo, e a função retorna True.

numeros_primos = [] # Cria uma lista vazia chamada numeros_primos para guardar os números primos encontrados
for n in range(1, 251): # Inicia um laço for que percorre todos os números de 1 até 250 (inclusive).
    #Verifica se n é primo chamando a função eh_primo(n)
    # Se for primo, adiciona n à lista numeros_primos.
    # Depois, imprime a lista atualizada (isso pode causar muitas impressões, uma por número primo — mais útil para depuração do que para uso final).
    if eh_primo(n):
        numeros_primos.append(n)
        print(numeros_primos)
# Salva os resultados em um arquivo, usando a função open a um manipulador
nome_arquivo = "results.txt"
with open(nome_arquivo, "w") as arquivo:
    arquivo.write("Números primos de 1 a 250:\n")
    for numero in numeros_primos:
        arquivo.write(f"{numero}, ")
        print(nome_arquivo)