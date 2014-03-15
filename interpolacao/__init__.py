from matplotlib.pyplot import subplot, xlabel, ylabel, show, figure
from functools import reduce
from numpy import linspace, float128


def _mostrar(grafico):
    quadro = grafico.get_position()

    grafico.set_position([quadro.x0, 
                          quadro.y0 + quadro.height * 0.1,
                          quadro.width, quadro.height * 0.9])

    grafico.legend(bbox_to_anchor=(0.5, -0.1),
                   loc='upper center', 
                   fancybox=True, 
                   shadow=True, 
                   ncol=5)

    xlabel(r"$x$")
    ylabel(r"$f(x)$")

    show()

def product(lista):
    return reduce(lambda acumulado, atual: acumulado * atual, lista)


def plotar_interpolacao(funcao, metodo, intervalo=(0, 1), pontos=100, pontos_entre_zeros=10):
    inicio, fim = intervalo
    
    x = linspace(float128(inicio), float128(fim), float128(pontos))
    y = [funcao(xi) for xi in x]

    interpolacao = metodo(x, y)

    x = linspace(float128(inicio), 
                 float128(fim), 
                 float128(pontos * pontos_entre_zeros))

    grafico = subplot()
    grafico.plot(x, [funcao(xi) for xi in x], label='Função')
    grafico.plot(x, [interpolacao(xi) for xi in x], label='Interpolação')
    _mostrar(grafico)
    

def plotar(*funcoes, intervalo=(0, 1), pontos=100):
    inicio, fim = intervalo

    x = linspace(float128(inicio), float128(fim), float128(pontos))

    grafico = subplot()
   
    for item in funcoes:
        funcao = item[0] if isinstance(item, tuple) else item
        descricao = item[1] if isinstance(item, tuple) else ''

        y = [funcao(xi) for xi in x]
        grafico.plot(x, y, label=descricao)

    _mostrar(grafico)
