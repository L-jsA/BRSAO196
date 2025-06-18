# LIÇÃO OITO - TIPOS DE DADOS COMPOSTOS 
import csv #Importa o módulo csv, que permite ler e escrever arquivos no formato CSV (Comma-Separated Values).
import copy #Importa o módulo copy, usado para fazer cópias profundas (deep copies) de objetos complexos, como dicionários aninhados.

meuVeiculo = { # Dicionário 
    "vin" : "<empty>", #número de identificação do veículo
    "make" : "<empty>" , #fabricante
    "model" : "<empty>" , #modelo
    "year" : 0, #ano
    "range" : 0, # autonomia (provavelmente em milhas ou km)
    "topSpeed" : 0, # velocidade máxima
    "zeroSixty" : 0.0, #tempo de 0 a 60 mph
    "mileage" : 0 # quilometragem
}

for key, value in meuVeiculo.items():  # Faz um loop por cada chave/valor do dicionário meuVeiculo e imprime os valores padrões.
    print("{} : {}".format(key,value))

meuInventario = [] # Inicializa uma lista vazia onde cada elemento será um veículo preenchido com dados reais.

with open('car_fleet.csv') as csvFile: #Abre o arquivo car_fleet.csv no modo leitura.
    csvReader = csv.reader(csvFile, delimiter=',')  #Cria um leitor CSV que interpreta cada linha como uma lista de strings, separadas por vírgula.
    lineCount = 0   #Inicializa um contador de linhas lidas do arquivo.
    for row in csvReader: #Primeira linha (linha 0) normalmente contém os nomes das colunas, então ela é apenas exibida.
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  # Exibe os dados de cada linha de forma organizada.
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            veiculoAtual = copy.deepcopy(meuVeiculo)  
            veiculoAtual["vin"] = row[0]  
            veiculoAtual["make"] = row[1]  
            veiculoAtual["model"] = row[2]  
            veiculoAtual["year"] = row[3]  #Preenche os campos do dicionário com os dados da linha atual do CSV.
            veiculoAtual["range"] = row[4]  
            veiculoAtual["topSpeed"] = row[5]  
            veiculoAtual["zeroSixty"] = row[6]  
            veiculoAtual["mileage"] = row[7]  
            meuInventario.append(veiculoAtual)  #Adiciona o dicionário preenchido à lista meuInventario e incrementa o contador de linhas.
            lineCount += 1  
    print(f'Processed {lineCount} lines.') #Exibe quantas linhas (incluindo o cabeçalho) foram processadas.

    veiculoAtual= copy.deepcopy(meuVeiculo) #Faz uma cópia independente do modelo de veículo (para evitar alterações no original).
    for myCarProperties in meuInventario: #Itera por todos os veículos do inventário (myCarProperties) e imprime todos os pares chave-valor de cada veículo, com uma linha de separação ----- entre as propriedades.
     for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")