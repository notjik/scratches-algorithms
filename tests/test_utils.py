from unittest import TestCase
from src.scratches_algorithms import utils


class TestDivisors(TestCase):
    def test_equal(self):
        self.assertEqual(utils.NumbersProperties.divisors(3335),
                         [1, 3335, 5, 667, 23, 145, 29, 115])
        self.assertEqual(utils.NumbersProperties.divisors(3335,
                                                          nontrivial=True),
                         [5, 667, 23, 145, 29, 115])
        self.assertEqual(utils.NumbersProperties.divisors(3335,
                                                          prime=True),
                         [5, 23, 29])
        self.assertEqual(utils.NumbersProperties.divisors(3335,
                                                          integer=True),
                         [1, 3335, 5, 667, 23, 145, 29, 115, -1, -3335, -5, -667, -23, -145, -29, -115])
        self.assertEqual(utils.NumbersProperties.divisors(3335,
                                                          nontrivial=True,
                                                          integer=True),
                         [5, 667, 23, 145, 29, 115, -5, -667, -23, -145, -29, -115])
        self.assertEqual(utils.NumbersProperties.divisors(-3335),
                         [1, 3335, 5, 667, 23, 145, 29, 115])
        self.assertEqual(utils.NumbersProperties.divisors(-3335,
                                                          nontrivial=True),
                         [5, 667, 23, 145, 29, 115])
        self.assertEqual(utils.NumbersProperties.divisors(-3335,
                                                          prime=True),
                         [5, 23, 29])
        self.assertEqual(utils.NumbersProperties.divisors(-3335,
                                                          integer=True),
                         [1, 3335, 5, 667, 23, 145, 29, 115, -1, -3335, -5, -667, -23, -145, -29, -115])
        self.assertEqual(utils.NumbersProperties.divisors(-3335,
                                                          nontrivial=True,
                                                          integer=True),
                         [5, 667, 23, 145, 29, 115, -5, -667, -23, -145, -29, -115])

    def test_raises(self):
        self.assertRaises(ZeroDivisionError,
                          utils.NumbersProperties.divisors, 0)
        self.assertRaises(TypeError,
                          utils.NumbersProperties.divisors,
                          1 / 3)
        self.assertRaises(TypeError,
                          utils.NumbersProperties.divisors,
                          3335j)
        self.assertRaises(ValueError,
                          utils.NumbersProperties.divisors,
                          3335,
                          prime=True,
                          nontrivial=True)
        self.assertRaises(ValueError,
                          utils.NumbersProperties.divisors,
                          3335,
                          prime=True,
                          integer=True)


class TestCountDivisors(TestCase):
    def test_equal(self):
        self.assertEqual(utils.NumbersProperties.count_divisors(3335),
                         8)
        self.assertEqual(utils.NumbersProperties.count_divisors(3335,
                                                                nontrivial=True),
                         6)
        self.assertEqual(utils.NumbersProperties.count_divisors(3335,
                                                                prime=True),
                         3)
        self.assertEqual(utils.NumbersProperties.count_divisors(3335,
                                                                integer=True),
                         16)
        self.assertEqual(utils.NumbersProperties.count_divisors(3335,
                                                                nontrivial=True,
                                                                integer=True),
                         12)
        self.assertEqual(utils.NumbersProperties.count_divisors(-3335),
                         8)
        self.assertEqual(utils.NumbersProperties.count_divisors(-3335,
                                                                nontrivial=True),
                         6)
        self.assertEqual(utils.NumbersProperties.count_divisors(-3335,
                                                                prime=True),
                         3)
        self.assertEqual(utils.NumbersProperties.count_divisors(-3335,
                                                                integer=True),
                         16)
        self.assertEqual(utils.NumbersProperties.count_divisors(-3335,
                                                                nontrivial=True,
                                                                integer=True),
                         12)

    def test_raises(self):
        self.assertRaises(ZeroDivisionError,
                          utils.NumbersProperties.count_divisors,
                          0)
        self.assertRaises(TypeError,
                          utils.NumbersProperties.count_divisors,
                          1 / 3)
        self.assertRaises(TypeError,
                          utils.NumbersProperties.count_divisors,
                          3335j)
        self.assertRaises(ValueError,
                          utils.NumbersProperties.count_divisors,
                          3335,
                          prime=True,
                          nontrivial=True)
        self.assertRaises(ValueError,
                          utils.NumbersProperties.count_divisors,
                          3335,
                          prime=True,
                          integer=True)


class TestFibonacci(TestCase):
    def test_equal(self):
        self.assertEqual(utils.NumbersProperties.fibonacci(0),
                         0)
        self.assertEqual(utils.NumbersProperties.fibonacci(2),
                         1)
        self.assertEqual(utils.NumbersProperties.fibonacci(4),
                         3)
        self.assertEqual(utils.NumbersProperties.fibonacci(8),
                         21)
        self.assertEqual(utils.NumbersProperties.fibonacci(16),
                         987)
        self.assertEqual(utils.NumbersProperties.fibonacci(32),
                         2178309)
        self.assertEqual(utils.NumbersProperties.fibonacci(64),
                         10610209857723)
        self.assertEqual(utils.NumbersProperties.fibonacci(128),
                         251728825683550554663419904)
        self.assertEqual(utils.NumbersProperties.fibonacci(256),
                         141693817714057722810263663060681563731249103013675008)

    def test_raises(self):
        self.assertRaises(TypeError,
                          utils.NumbersProperties.fibonacci,
                          True)
        self.assertRaises(TypeError,
                          utils.NumbersProperties.fibonacci,
                          '256')
        self.assertRaises(TypeError,
                          utils.NumbersProperties.fibonacci,
                          1.1)
        self.assertRaises(TypeError,
                          utils.NumbersProperties.fibonacci,
                          3j)
        self.assertRaises(ValueError,
                          utils.NumbersProperties.fibonacci,
                          -1)


class TestIsPrime(TestCase):
    def test_equal(self):
        self.assertEqual(utils.NumbersProperties.is_prime(-2),
                         False)
        self.assertEqual(utils.NumbersProperties.is_prime(-1),
                         False)
        self.assertEqual(utils.NumbersProperties.is_prime(0),
                         False)
        self.assertEqual(utils.NumbersProperties.is_prime(1),
                         False)
        self.assertEqual(utils.NumbersProperties.is_prime(2),
                         True)
        self.assertEqual(utils.NumbersProperties.is_prime(3571),
                         True)

    def test_raises(self):
        self.assertRaises(TypeError,
                          utils.NumbersProperties.is_prime,
                          True)
        self.assertRaises(TypeError,
                          utils.NumbersProperties.is_prime,
                          1.1)
        self.assertRaises(TypeError,
                          utils.NumbersProperties.is_prime,
                          3j)
        self.assertRaises(TypeError,
                          utils.NumbersProperties.is_prime,
                          '256')


class TestIsSquare(TestCase):
    def test_equal(self):
        self.assertEqual(utils.NumbersProperties.is_square(-2),
                         False)
        self.assertEqual(utils.NumbersProperties.is_square(2),
                         False)
        self.assertEqual(utils.NumbersProperties.is_square(4),
                         True)
        self.assertEqual(utils.NumbersProperties.is_square(9801),
                         True)

    def test_raises(self):
        self.assertRaises(TypeError,
                          utils.NumbersProperties.is_square,
                          True)
        self.assertRaises(TypeError,
                          utils.NumbersProperties.is_square,
                          1.1)
        self.assertRaises(TypeError,
                          utils.NumbersProperties.is_square,
                          3j)
        self.assertRaises(TypeError,
                          utils.NumbersProperties.is_square,
                          '256')


class TestToBase(TestCase):
    def test_equal(self):
        self.assertEqual(utils.NumeralSystem.to_base(0, 2),
                         '0')
        self.assertEqual(utils.NumeralSystem.to_base(1, 2),
                         '1')
        self.assertEqual(utils.NumeralSystem.to_base(2, 2),
                         '10')
        self.assertEqual(utils.NumeralSystem.to_base(3, 2),
                         '11')
        self.assertEqual(utils.NumeralSystem.to_base(4, 2),
                         '100')
        self.assertEqual(utils.NumeralSystem.to_base(0, 3),
                         '0')
        self.assertEqual(utils.NumeralSystem.to_base(1, 3),
                         '1')
        self.assertEqual(utils.NumeralSystem.to_base(2, 3),
                         '2')
        self.assertEqual(utils.NumeralSystem.to_base(3, 3),
                         '10')
        self.assertEqual(utils.NumeralSystem.to_base(4, 3),
                         '11')
        self.assertEqual(utils.NumeralSystem.to_base(42, 6),
                         '110')
        self.assertEqual(utils.NumeralSystem.to_base(8142, 9),
                         '12146')
        self.assertEqual(utils.NumeralSystem.to_base(51614, 12),
                         '25a52')
        self.assertEqual(utils.NumeralSystem.to_base(-51614, 12),
                         '-25a52')
        self.assertEqual(utils.NumeralSystem.to_base(0, 2, bits=8),
                         '00000000')
        self.assertEqual(utils.NumeralSystem.to_base(1, 2, bits=9),
                         '000000001')
        self.assertEqual(utils.NumeralSystem.to_base(2, 2, bits=10),
                         '0000000010')
        self.assertEqual(utils.NumeralSystem.to_base(3, 2, bits=11),
                         '00000000011')
        self.assertEqual(utils.NumeralSystem.to_base(4, 2, bits=12),
                         '000000000100')
        self.assertEqual(utils.NumeralSystem.to_base(0, 3, bits=13),
                         '0000000000000')
        self.assertEqual(utils.NumeralSystem.to_base(1, 3, bits=14),
                         '00000000000001')
        self.assertEqual(utils.NumeralSystem.to_base(2, 3, bits=15),
                         '000000000000002')
        self.assertEqual(utils.NumeralSystem.to_base(3, 3, bits=16),
                         '0000000000000010')
        self.assertEqual(utils.NumeralSystem.to_base(4, 3, bits=17),
                         '00000000000000011')
        self.assertEqual(utils.NumeralSystem.to_base(42, 6, bits=18),
                         '000000000000000110')
        self.assertEqual(utils.NumeralSystem.to_base(8142, 9, bits=19),
                         '0000000000000012146')
        self.assertEqual(utils.NumeralSystem.to_base(51614, 12, bits=20),
                         '00000000000000025a52')
        self.assertEqual(utils.NumeralSystem.to_base(-51614, 12, bits=20),
                         '-00000000000000025a52')

    def test_raises(self):
        self.assertRaises(TypeError,
                          utils.NumeralSystem.to_base,
                          True,
                          True)
        self.assertRaises(TypeError,
                          utils.NumeralSystem.to_base,
                          True,
                          True,
                          bits=True)
        self.assertRaises(TypeError,
                          utils.NumeralSystem.to_base,
                          True,
                          True,
                          bits=8)
        self.assertRaises(TypeError,
                          utils.NumeralSystem.to_base,
                          12415,
                          True)
        self.assertRaises(TypeError,
                          utils.NumeralSystem.to_base,
                          12415,
                          True,
                          bits=True)
        self.assertRaises(TypeError,
                          utils.NumeralSystem.to_base,
                          12415,
                          True,
                          bits=8)
        self.assertRaises(TypeError,
                          utils.NumeralSystem.to_base,
                          True,
                          30,
                          bits=True)
        self.assertRaises(TypeError,
                          utils.NumeralSystem.to_base,
                          True,
                          30,
                          bits=8)
        self.assertRaises(TypeError,
                          utils.NumeralSystem.to_base,
                          12415,
                          30,
                          bits=True)
        self.assertRaises(TypeError,
                          utils.NumeralSystem.to_base,
                          1.1,
                          30)
        self.assertRaises(TypeError,
                          utils.NumeralSystem.to_base,
                          3j,
                          30)
        self.assertRaises(TypeError,
                          utils.NumeralSystem.to_base,
                          12415,
                          1.1)
        self.assertRaises(TypeError,
                          utils.NumeralSystem.to_base,
                          12415,
                          30,
                          bits=1.1)
        self.assertRaises(TypeError,
                          utils.NumeralSystem.to_base,
                          12415,
                          30,
                          bits=3j)
        self.assertRaises(TypeError,
                          utils.NumeralSystem.to_base,
                          12415,
                          3j)
        self.assertRaises(ValueError,
                          utils.NumeralSystem.to_base,
                          12415,
                          15156)
        self.assertRaises(ValueError,
                          utils.NumeralSystem.to_base,
                          12415,
                          15156)
        self.assertRaises(ValueError,
                          utils.NumeralSystem.to_base,
                          12415,
                          30,
                          bits=-8)

