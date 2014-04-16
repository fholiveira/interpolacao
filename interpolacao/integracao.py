from interpolacao import product
from numpy import linalg, linspace

def ponto_medio(funcao, inicio, fim):
    return (fim - inicio) * funcao((inicio + fim) / 2)

def trapezios(funcao, inicio, fim):
    return (funcao(inicio) + funcao(fim)) * (fim - inicio) * 1/2

def simpson_um_terco(funcao, inicio, fim):
    intervalo = linspace(float(inicio), float(fim), 3.0)
    somatorio = [funcao(intervalo[0]),
                 4 * funcao(intervalo[1]),
                 funcao(intervalo[2])]

    return somatorio * ((fim - inicio) / 2) * 1/3

def simpson_tres_oitavos(funcao, inicio, fim):
    intervalo = linspace(float(inicio), float(fim), 4.0)
    somatorio = [funcao(intervalo[0]),
                 3 * funcao(intervalo[1]),
                 3 * funcao(intervalo[2]),
                 funcao(intervalo[3])]

    return somatorio * ((fim - inicio) / 3) * 3/8

def ponto_medio_composta(funcao, inicio, fim, pontos=100):
    x = linspace(float(inicio), float(fim), float(pontos))
    
    somatorio = [funcao((x[i - 1] + x[i]) / 2) for i in range(1, pontos)]

    return sum(somatorio) * ((fim - inicio) / pontos)
    
def trapezios_composta(funcao, inicio, fim, pontos=100):
    intervalo = linspace(float(inicio), float(fim), float(pontos))
    
    somatorio = [funcao(intervalo[0])] + [2 * funcao(xi) for xi in intervalo[1:-1]] + [funcao(intervalo[-1])]

    return sum(somatorio) * ((fim - inicio) / pontos) * 1/2
