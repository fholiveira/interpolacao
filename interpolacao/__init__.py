from functools import reduce

def product(lista):
    return reduce(lambda acumulado, atual: acumulado * atual, lista)
