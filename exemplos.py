from interpolacao import plotar, plotar_interpolacao
from interpolacao.metodos import newton, lagrange

#plotando vária funções
plotar((lambda x: x**2, 'Quadrática'),
       (lambda x: x**3, 'Cúbica'))

#plotando uma função e comparando com ela interpolada pelo método de newton
plotar_interpolacao(lambda x: 1 / (1 + x**2), 
                    lagrange, 
                    intervalo=(-5, 5), 
                    pontos=10)
