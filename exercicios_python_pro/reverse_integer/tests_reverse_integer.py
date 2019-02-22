from unittest import TestCase, main
from reverse_integer import reverse_integer


class TestReversePositiveInteger(TestCase):
    def test_321_should_return_123(self):
        expected = 321
        self.assertEqual(expected, reverse_integer(123))

    def test_negative_321_should_return_negative_123(self):
        expected = -321
        self.assertEqual(expected, reverse_integer(-123))

    def test_3334_should_return_4333(self):
        expected = 4333
        self.assertEqual(expected, reverse_integer(3334))

    def test_negative_334_shoul_return_negative_433(self):
        expected = -433
        self.assertEqual(expected, reverse_integer(-334))

    def test_1534236469_should_return_0(self):
        expected = 0
        self.assertEqual(expected, reverse_integer(1534236469))


if __name__ == '__main__':
    main()
