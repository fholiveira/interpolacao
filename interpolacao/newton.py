from functools import reduce

def newton(x, fx):
    calcula = lambda index, ordem: (y[index + 1] - y[index]) / (x[index + ordem] - x[index])

    tab = [fx]
    for ordem in range(1, len(x)):
        y = tab[ordem - 1]
        tab.append([calcula(index, ordem) for index in range(0, len(x) - ordem)])

    y = [a[0] for a in tab] 

    def funcao(numero):
        mult = [numero - xi for xi in x]
        somatorio = lambda n: reduce(lambda t, a: t * a, mult[:n])
        return sum(somatorio(index + 1) * yi for index, yi in enumerate(y[1:])) + fx[0]

    return funcao
