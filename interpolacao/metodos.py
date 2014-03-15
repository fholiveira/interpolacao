from interpolacao import product

def newton(x, fx):
    tabela_de_deltas = [fx]
    for ordem in range(1, len(x)):
        y = tabela_de_deltas[ordem - 1]

        delta_ordem = [(y[i + 1] - y[i]) / (x[i + ordem] - x[i]) 
                       for i in range(0, len(x) - ordem)] 

        tabela_de_deltas.append(delta_ordem)

    deltas = [delta[0] for delta in tabela_de_deltas] 

    return lambda num: sum(product([num - xi for xi in x[:i]] or [1]) * yi 
                       for i, yi in enumerate(deltas))
