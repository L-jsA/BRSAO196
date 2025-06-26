# EXERCÍCIO DA CALCULADORA

# OPERADORES: soma(+), subtração(-), multiplicação(*), divisão(/)

def calculadora(numero1, numero2, operacao):
    if operacao == "+":
        return numero1 + numero2
    elif operacao == "-":
        return numero1 - numero2
    elif operacao == "*":
        return numero1 * numero2
    elif operacao == "/":
        try:
            return numero1 / numero2
        except ZeroDivisionError:
            return "Erro, não é possível realizar divisão por ZERO!"
    else:
        return "Operação inválida!"
try:
    numero1 = float(input("Digite o primeiro número: ")) # Exibe a mensagem "Digite o primeiro número: " para o usuário.
    # input: pega o que o usuário digita como uma string. 
    # float: tenta converter esse valor para um número decimal
    numero2 = float(input("Digite o segundo número: ")) # faz a mesma coisa que o "numero1"
    operacao = input("Digite a operação (+, -, *, /): ") # Solicita ao usuário que digite uma operação matemática. Armazena a resposta como uma string (por exemplo: "+", "-", "*" ou "/").

    resultado = calculadora(numero1, numero2, operacao) # Chama uma função chamada calculadora (que precisa estar definida em algum lugar do seu código).
    # Passa os dois números e o operador como argumentos.
    # Armazena o resultado da função na variável resultado.
    print("Resultado: ", resultado) # Exibe na tela o resultado retornado pela função calculadora.
except ValueError: # Se ocorrer um erro de conversão de string para número (por exemplo, o usuário digita "abc" em vez de um número), essa parte será executada.
    # ValueError é o tipo de erro que ocorre quando tentamos converter algo que não pode ser transformado em número (float("abc")).
    print("Erro: digite um número valido.") # Mostra uma mensagem de erro amigável para o usuário, se o erro ValueError for capturado.