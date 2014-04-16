from math import e, cos, sin, pi
from interpolacao import plotar, plotar_interpolacao
from interpolacao.metodos import newton, lagrange, polinomial
from interpolacao.integracao import (ponto_medio, ponto_medio_composta, trapezios,
                                     trapezios_composta, simpson_tres_oitavos,
                                     simpson_um_terco)

# plotando vária funções
# plotar((lambda x: x**2, 'Quadrática'),
#       (lambda x: x**3, 'Cúbica'))

# plotando uma função e comparando com ela interpolada pelo método de newton
plotar_interpolacao(lambda x: 1 / (1 + x ** 2),
                    polinomial,
                    intervalo=(-5, 5),
                    pontos=10,
                    pontos_entre_zeros=100)

#calcular integral usando o metodo de trapezios composto
funcao = lambda x: e ** x
aproximacao = trapezios_composta(lambda x: e ** x, 1, 3, pontos=200)
valor_exato = funcao(3) - funcao(1)
erro = valor_exato - aproximacao

print('Aproximando e^x no intervalo de 1 a 3 usando 200 pontos:')
print('Valor exato:', valor_exato)
print('Aproximação:', aproximacao)
print('Erro:', erro)
