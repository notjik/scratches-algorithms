"""
A module for testing the package validator.

-----

:author: notjik
:license: MIT License
:copyright: (c) 2023 notjik
"""
from unittest import TestCase
from src.scratches_algorithms._validator import _is_valid_bool, _is_valid_int, _is_valid_sequence


class TestIsValidBool(TestCase):
    def test(self):
        self.assertIsNone(_is_valid_bool(1 == 1, 1 < 1))
        self.assertIsNone(_is_valid_bool([1] == [1], [1] < [1]))
        self.assertIsNone(_is_valid_bool('1' == '1', '1' < '1'))

    def test_raises(self):
        self.assertRaises(TypeError,
                          _is_valid_bool,
                          1 == 1, 1 > 1, 1)
        self.assertRaises(TypeError,
                          _is_valid_bool,
                          1 == 1, 1 > 1, [1 == 1, 1 > 1])
        self.assertRaises(TypeError,
                          _is_valid_bool,
                          '1' == '1', '1' > '1', '1 == 1', '1 > 1')
        self.assertRaises(TypeError,
                          _is_valid_bool,
                          1, 2, 3, 4, 5)
        self.assertRaises(TypeError,
                          _is_valid_bool,
                          1j, 2j, 3j, 4j, 5j)
        self.assertRaises(TypeError,
                          _is_valid_bool,
                          1., 2., 3., 4., 5.)


class TestIsValidInt(TestCase):
    def test(self):
        self.assertIsNone(_is_valid_int(1, 2, 3, 4, 5))

    def test_raises(self):
        self.assertRaises(TypeError,
                          _is_valid_int,
                          1, 2, 1 < 2)
        self.assertRaises(TypeError,
                          _is_valid_int,
                          1, 2, [1, 2])
        self.assertRaises(TypeError,
                          _is_valid_int,
                          1, 2, '1', '2')
        self.assertRaises(TypeError,
                          _is_valid_int,
                          1j, 2j, 3j, 4j, 5j)
        self.assertRaises(TypeError,
                          _is_valid_int,
                          1., 2., 3., 4., 5.)


class TestIsValidSequence(TestCase):
    def test(self):
        self.assertIsNone(_is_valid_sequence([1, 2, 3, 4, 5],
                                             [1j, 2j, 3j, 4j, 5j],
                                             [1., 2., 3., 4., 5.],
                                             [1 == 1, 2 < 3, 4 > 5],
                                             ['1', '2', '3', '4', '5'],
                                             '12345'))
        self.assertIsNone(_is_valid_sequence([1, 2, 3, 4, 5],
                                             [1j, 2j, 3j, 4j, 5j],
                                             [1., 2., 3., 4., 5.],
                                             [1 == 1, 2 < 3, 4 > 5],
                                             ['1', '2', '3', '4', '5'],
                                             closed=[str]))

    def test_raises(self):
        self.assertRaises(TypeError,
                          _is_valid_sequence,
                          1, 2, 3, 4, 5)
        self.assertRaises(TypeError,
                          _is_valid_sequence,
                          1j, 2j, 3j, 4j, 5j)
        self.assertRaises(TypeError,
                          _is_valid_sequence,
                          1., 2., 3., 4., 5.)
        self.assertRaises(TypeError,
                          _is_valid_sequence,
                          1 == 1, 2 < 3, 4 > 5)
        self.assertRaises(TypeError,
                          _is_valid_sequence,
                          [1, 2, 3, 4, 5],
                          [1j, 2j, 3j, 4j, 5j],
                          [1., 2., 3., 4., 5.],
                          [1 == 1, 2 < 3, 4 > 5],
                          ['1', '2', '3', '4', '5'],
                          '12345',
                          closed=[str])
