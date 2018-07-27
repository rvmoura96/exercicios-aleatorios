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


def check_collatz(number):
    if number % 2 != 0:
        return (number * 3) + 1
    return number // 2


def collatz_sequence(number):
    sequence = [number]
    new_number = number
    while new_number != 1:
        new_number = check_collatz(new_number)
        sequence.append(new_number)
    return sequence


def collatz_sequence_len(number):
    return len(collatz_sequence(number))
