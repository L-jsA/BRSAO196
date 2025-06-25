# DICIONÁRIO

# PRIMEIRA FORMA 
dic = {
    "um": 1,
    "dois": 2,
    "três": 3,
    "quatro": 4
}

print("O terceiro valor é:", dic["três"])
print ("\n Toodo o dicionário:")
print(dic)
 
# SEGUNDA FORMA
for chave, valor in dic.items(): 
    print(f"Chave: {chave} > Valor: {valor}")