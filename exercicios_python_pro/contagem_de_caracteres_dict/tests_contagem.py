from unittest import TestCase, main
from contar_caracteres_dict import contagem_caracteres


class TestContagemCaracteres(TestCase):

    def test_string_ovo(self):
        esperado = {'o': 2, 'v': 1}

        self.assertEqual(esperado, contagem_caracteres('ovo'))

    def test_string_renan(self):
        esperado = {'a': 1, 'e': 1, 'n': 2, 'r': 1}

        self.assertEqual(esperado, contagem_caracteres('renan'))

    def test_string_grrr(self):
        esperado = {'g': 1, 'r': 3}
        self.assertEqual(esperado, contagem_caracteres('grrr'))


if __name__ == '__main__':
    main()
