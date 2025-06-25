# EXCEÇÕES

# EXCEÇÃO 1
'''x = 10 / 0
print(x)
try:
    x = 10 / 0
except ZeroDivisionError: # # EXCEÇÃO 1, pois não se pode dividir nenhum número por 0
    print("Você não pode dividir por ZERO")'''

# EXCEÇÃO 2
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print("Resultado: ", resultado)
except ValueError: # Trata algum erro possível
    print("Número invalido")
except ZeroDivisionError: # Trata algum erro possível
    print("Impossivel dividir por zero")