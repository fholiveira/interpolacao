from interpolacao.metodos import lagrange
from unittest import TestCase

class TestLagrange(TestCase):
    def test_interpola_pontos_conhecidos(self):
        funcao = lagrange([00000, 0.200, 0.300, 0.500, 0.600], 
                          [1.008, 1.064, 1.125, 1.343, 1.512])

        self.assertAlmostEqual(1.008, funcao(0.0))
        self.assertAlmostEqual(1.064, funcao(0.2))
        self.assertAlmostEqual(1.125, funcao(0.3))
        self.assertAlmostEqual(1.343, funcao(0.5))
        self.assertAlmostEqual(1.512, funcao(0.6))

    def test_interpola_funcao_2o_grau(self):
        tabela = {x: 3.0 * x**2 + 4.3 * x + 7.0 for x in [1.0, 3.4, 4.7, 6.0]}

        funcao = lagrange(list(tabela.keys()), list(tabela.values()))

        self.assertAlmostEqual(tabela[1.0], funcao(1.0))
        self.assertAlmostEqual(tabela[3.4], funcao(3.4))
        self.assertAlmostEqual(tabela[4.7], funcao(4.7))
        self.assertAlmostEqual(tabela[6.0], funcao(6.0))

    def test_interpola_funcao_1o_grau(self):
        tabela = {x: 0.34 * x + 3.56 for x in [0.9, 2.6, 2.8, 3.0]}

        funcao = lagrange(list(tabela.keys()), list(tabela.values()))

        self.assertAlmostEqual(tabela[0.9], funcao(0.9))
        self.assertAlmostEqual(tabela[2.6], funcao(2.6))
        self.assertAlmostEqual(tabela[2.8], funcao(2.8))
        self.assertAlmostEqual(tabela[3.0], funcao(3.0))
