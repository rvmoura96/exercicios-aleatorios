"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
from unittest import TestCase, main
from add_two_numbers import add_two_numbers


class TestAddTwoNumbers(TestCase):
    def test_2_4_3_add_5_6_4(self):
        esperado = [8, 0, 7]
        self.assertEqual(esperado, add_two_numbers([2, 4, 3], [5, 6, 4]))

    def test_2_4_2_add_5_6_1(self):
        esperado = [8, 0, 3]
        self.assertEqual(esperado, add_two_numbers([2, 4, 2], [5, 6, 1]))


if __name__ == '__main__':
    main()
