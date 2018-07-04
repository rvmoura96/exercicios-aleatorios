"""Enunciado do exercício.
Analisando a conjectura de Collatz
Você está resolvendo este problema.

Este problema foi utilizado em 223 Dojo(s).

Para definir uma seqüência a partir de um número inteiro o positivo, temos as seguintes regras:

n → n/2 (n é par)

n → 3n + 1 (n é ímpar)

Usando a regra acima e iniciando com o número 13, geramos a seguinte seqüência:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Podemos ver que esta seqüência (iniciando em 13 e terminando em 1) contém 10 termos. Embora ainda não tenha sido provado (este problema é conhecido como Problema de Collatz), sabemos que com qualquer número que você começar, a seqüência resultante chega no número 1 em algum momento.

Desenvolva um programa que descubra qual o número inicial entre 1 e 1 milhão que produz a maior seqüência.
"""
from unittest import TestCase, main
from collatz import check_collatz, collatz_sequence, collatz_sequence_len


class TestPares(TestCase):
    def test_40_must_return_20(self):
        self.assertEqual(check_collatz(40), 20)

    def test_20_must_return_10(self):
        self.assertEqual(check_collatz(10), 5)

    def test_16_must_return_8(self):
        self.assertEqual(check_collatz(16), 8)


class TestImpares(TestCase):
    def test_5_must_return_16(self):
        self.assertEqual(check_collatz(5), 16)

    def test_13_must_return_40(self):
        self.assertEqual(check_collatz(13), 40)

    def test_15_must_return_46(self):
        self.assertEqual(check_collatz(15), 46)


class TestSequenciaCollatz(TestCase):
    def test_13(self):
        self.assertEqual(collatz_sequence(13), [13, 40, 20, 10, 5, 16, 8, 4,
                                                2, 1])

    def test_22(self):
        self.assertEqual(collatz_sequence(22), [22, 11, 34, 17, 52, 26, 13,
                                                40, 20, 10, 5, 16, 8, 4, 2,
                                                1])

    def test_7(self):
        self.assertEqual(collatz_sequence(6), [6, 3, 10, 5, 16, 8, 4, 2, 1])


class TestSizeCollatzLen(TestCase):
    def test_size_when_22_must_be_16(self):
        self.assertEqual(collatz_sequence_len(22), 16)


if __name__ == '__main__':
    main()