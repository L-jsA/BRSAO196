#LIÇÃO SETE - CATEGORIZAR VALORES

listaMista = [45, 290578, 1.02, True, "Meu cachorro está na cama.", "45"] # lista com vários tipos de dados

for list in listaMista: # percorre a lista
    print("{} é do tipo de dado {}".format(list, type(list))) # imprime cada lista, o dado, e seu tipo.
                                                              # .format está formatando as chaves com o elemento e valor correto 