"""
author: notjik
license: MIT License

copyright: (C) 2023 notjik
"""
from time import perf_counter
from typing import Callable, Any

__all__ = ['NumbersProperties',
           'NumeralSystem',
           'PerformanceTracking']


class NumbersProperties:
    @staticmethod
    # TODO: Search for divisors
    # TODO: Поиск делителей
    def divisors(number: int, *, nontrivial: bool = False, prime: bool = False, integer: bool = False) -> list:
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError('The current {} type is {}, expected int'.format(number, type(number).__name__))
        elif not isinstance(nontrivial, bool):
            raise TypeError('The current {} type is {}, expected bool'.format(nontrivial, type(nontrivial).__name__))
        elif not isinstance(prime, bool):
            raise TypeError('The current {} type is {}, expected bool'.format(prime, type(prime).__name__))
        elif not isinstance(integer, bool):
            raise TypeError('The current {} type is {}, expected bool'.format(integer, type(integer).__name__))
        elif number == 0:
            raise ZeroDivisionError('It is impossible to find divisors for zero')
        elif all((prime, nontrivial)):
            raise ValueError('It is impossible to find nontrivial prime divisors')
        elif all((prime, integer)):
            raise ValueError('It is impossible to find prime divisors in integers')
        else:
            result = []
        i = 1 if not (nontrivial or prime) else 2
        tmp_number = abs(number)
        if prime:
            while i ** 2 <= tmp_number:
                if tmp_number % i == 0:
                    result.append(i)
                    tmp_number //= i
                else:
                    i += 1
            if tmp_number > 1:
                result.append(tmp_number)
        else:
            while i ** 2 <= tmp_number:
                if i ** 2 == tmp_number:
                    result.append(i)
                elif tmp_number % i == 0:
                    result += [i, tmp_number // i]
                i += 1
        return result if not integer else result + list(map(lambda x: -x, result))

    @staticmethod
    # TODO: Finding the number of divisors (through the basic theorem of arithmetic)
    # TODO: Нахождение количества делителей (через основную теорему арифметики)
    def count_divisors(number: int, *, nontrivial: bool = False, prime: bool = False, integer: bool = False):
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError('The current {} type is {}, expected int'.format(number, type(number).__name__))
        elif not isinstance(nontrivial, bool):
            raise TypeError('The current {} type is {}, expected bool'.format(nontrivial, type(nontrivial).__name__))
        elif not isinstance(prime, bool):
            raise TypeError('The current {} type is {}, expected bool'.format(prime, type(prime).__name__))
        elif not isinstance(integer, bool):
            raise TypeError('The current {} type is {}, expected bool'.format(integer, type(integer).__name__))
        elif number == 0:
            raise ZeroDivisionError('It is impossible to find divisors for zero')
        elif all((prime, nontrivial)):
            raise ValueError('It is impossible to find the count of nontrivial prime divisors')
        elif all((prime, integer)):
            raise ValueError('It is impossible to find the count prime divisors in integers')
        else:
            result = 1
        prime_divisors = NumbersProperties.divisors(abs(number), prime=True)
        if not prime:
            for i in set(prime_divisors):
                result *= prime_divisors.count(i) + 1
            if integer:
                result *= 2
            return result if not nontrivial else result - 2 if not integer else result - 4
        else:
            result = len(prime_divisors)
            return result

    @staticmethod
    # TODO: Finding the n-th term of the Fibonacci number (via the Binet's formula)
    # TODO: Нахождение n-го члена числа Фибоначчи (через формулу Бине)
    def fibonacci(number: int) -> int:
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError('The current {} type is {}, expected int'.format(number, type(number).__name__))
        elif number < 0:
            raise ValueError('The n-th term of the sequence must be greater than 0')
        return round((((1 + 5 ** 0.5) / 2) ** number - ((1 - 5 ** 0.5) / 2) ** number) / 5 ** 0.5)

    @staticmethod
    # TODO: Checking a number for prime
    # TODO: Проверка числа на простоту
    def is_prime(number: int) -> bool:
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError('The current {} type is {}, expected int'.format(number, type(number).__name__))
        if number < 2:
            return False
        i = 2
        while i * i <= number:
            if number % i == 0:
                return False
            i += 1
        return True

    @staticmethod
    # TODO: Checking the number by square
    # TODO: Проверка числа на квадрат
    def is_square(number: int) -> bool:
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError('The current {} type is {}, expected int'.format(number, type(number).__name__))
        elif number < 0:
            return False
        return (number ** 0.5) % 1 == 0


class NumeralSystem:
    @staticmethod
    # TODO: Conversion from decimal to any other number system (from binary to thirty-six-bit)
    # TODO: Перевод из десятичной системы счисления в любую другую (от двоичной до тридцатишестиричной)
    def to_base(number: int, base: int, *, bits: int = -1) -> str:
        if not isinstance(number, int) or isinstance(number, bool):
            raise TypeError('The current {} type is {}, expected int'.format(number, type(number).__name__))
        elif not isinstance(base, int) or isinstance(base, bool):
            raise TypeError('The current {} type is {}, expected int'.format(base, type(base).__name__))
        elif not isinstance(bits, int) or isinstance(bits, bool):
            raise TypeError('The current {} type is {}, expected int'.format(bits, type(bits).__name__))
        elif not 2 <= base <= 36:
            raise ValueError('The base number system must be positive')
        elif bits != -1 and bits <= 0:
            raise ValueError('The number of bits must be positive')
        negative = False
        if number < 0:
            negative = True
            number = abs(number)
        alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
        result = alphabet[number % base]
        while number >= base:
            number //= base
            result += alphabet[number % base]
        return ('-' if negative else '') + result[::-1] if bits == -1 else \
            ('-' if negative else '') + (result + ('0' * (bits - len(result))))[:bits][::-1]


class PerformanceTracking:
    # TODO: Initialization of the class, the beginning of the countdown
    # TODO: Инициализация класса, начало отсчёта
    def __init__(self, *, expected: int = 60) -> None:
        if not isinstance(expected, int) or isinstance(expected, bool):
            raise TypeError('The current {} type is {}, expected int'.format(expected, type(expected).__name__))
        self.start = perf_counter()
        self.expected = expected

    # TODO: Object deletion, end of countdown
    # TODO: Удаление объекта, окончание отсчёта
    def __del__(self) -> None:
        result = perf_counter() - self.start
        print('\nThe program was completed in \033[1m{}{}\033[0m second!'.format('\033[32m'
                                                                                 if result <= self.expected
                                                                                 else '\033[31m',
                                                                                 result))

    @staticmethod
    # TODO: A decorated function for calculating the time of operation of the function
    # TODO: Декорируемая функция для вычисления времени работы функции
    def func_timer(*, expected: int = 10) -> Any:
        def decorator(func: Callable) -> Any:
            def wrapper(*args, **kwargs) -> Any:
                start = perf_counter()
                call = func(*args, **kwargs)
                result = perf_counter() - start
                print('Function «{}» was completed in \033[1m{}{}\033[0m second!\n'.format(func.__name__,
                                                                                           '\033[32m'
                                                                                           if result <= expected
                                                                                           else '\033[31m',
                                                                                           result))
                return call

            return wrapper

        return decorator
