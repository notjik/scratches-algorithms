"""
A module with utilities for working with numbers, number systems and for analyzing code performance.

-----

:author: notjik
:license: MIT License
:copyright: (c) 2023 notjik
"""
from time import perf_counter
from sys import getsizeof
from typing import Callable, Any
from functools import wraps

from ._validator import _is_valid_int, _is_valid_bool

__all__ = ['NumbersProperties',
           'NumeralSystem',
           'PerformanceTracking']


class NumbersProperties:
    @staticmethod
    def divisors(number: int, *,
                 nontrivial: bool = False,
                 prime: bool = False,
                 all_prime: bool = False,
                 integer: bool = False) -> list:
        """
        Search for divisors
        :param number: an integer to be entered for analysis
        :param nontrivial: optional boolean value to indicate the search for non-trivial divisors, false by default
        :param prime: optional boolean value to indicate the search for prime divisors, false by default
        :param all_prime: optional boolean value to indicate the search for all prime divisors (with repetitions), false by default
        :param integer: optional boolean value to indicate a search in a set of integers, false by default
        :return: a list of divisors, taking into account the specified boolean values
        """
        _is_valid_int(number)
        _is_valid_bool(nontrivial, prime, all_prime, integer)
        if number == 0:
            raise ZeroDivisionError('It is impossible to find divisors for zero')
        elif all((prime, nontrivial)) or all((all_prime, nontrivial)):
            raise ValueError('It is impossible to find nontrivial prime divisors')
        elif all((prime, integer)) or all((all_prime, integer)):
            raise ValueError('It is impossible to find prime divisors in integers')
        elif all((prime, all_prime)):
            raise ValueError("You can't search for prime divisors and all prime divisors at the same time")
        result = []
        i = 1 if not (nontrivial or prime or all_prime) else 2
        tmp_number = abs(number)
        if all_prime or prime:
            while i ** 2 <= tmp_number:
                if tmp_number % i == 0:
                    result.append(i)
                    tmp_number //= i
                else:
                    i += 1
            if tmp_number > 1:
                result.append(tmp_number)
            if prime:
                result = list(set(result))
        else:
            while i ** 2 <= tmp_number:
                if i ** 2 == tmp_number:
                    result.append(i)
                elif tmp_number % i == 0:
                    result += [i, tmp_number // i]
                i += 1
        return result if not integer else result + list(map(lambda x: -x, result))

    @staticmethod
    def count_divisors(number: int, *,
                       nontrivial: bool = False,
                       prime: bool = False,
                       all_prime: bool = False,
                       integer: bool = False):
        """
        Finding the number of divisors
        :param number: an integer to be entered for analysis
        :param nontrivial: optional boolean value to denote the search for nontrivial divisors, false by default
        :param prime: optional boolean value to denote the search for prime divisors, false by default
        :param all_prime: optional boolean value to denote the search for all prime divisors (with repetitions), false by default
        :param integer: optional boolean value for denoting a search in a set of integers, false by default
        :return: an integer of the number of divisors that takes into account the specified boolean values
        """
        _is_valid_int(number)
        _is_valid_bool(nontrivial, prime, all_prime, integer)
        if number == 0:
            raise ZeroDivisionError('It is impossible to find divisors for zero')
        elif all((prime, nontrivial)) or all((all_prime, nontrivial)):
            raise ValueError('It is impossible to find the count of nontrivial prime divisors')
        elif all((prime, integer)) or all((all_prime, integer)):
            raise ValueError('It is impossible to find the count prime divisors in integers')
        elif all((prime, all_prime)):
            raise ValueError("You can't search for prime divisors and all prime divisors at the same time")
        prime_divisors = NumbersProperties.divisors(abs(number), all_prime=True)
        if not prime and not all_prime:
            result = 1
            for i in set(prime_divisors):
                result *= prime_divisors.count(i) + 1
            if integer:
                result *= 2
            return result if not nontrivial else result - 2 if not integer else result - 4
        else:
            return len(prime_divisors) if all_prime else len(set(prime_divisors))

    @staticmethod
    def fibonacci(number: int) -> int:
        """
        Finding the n-th term of the Fibonacci number
        :param number: an integer to be entered for analysis
        :return: an integer value of the nth Fibonacci number
        """
        _is_valid_int(number)
        if number < 0:
            raise ValueError('The n-th term of the sequence must be greater than 0')
        return round((((1 + 5 ** 0.5) / 2) ** number - ((1 - 5 ** 0.5) / 2) ** number) / 5 ** 0.5)

    @staticmethod
    def is_prime(number: int) -> bool:
        """
        Checking a number for prime
        :param number: an integer to be entered for analysis
        :return: a boolean value of matching a number with a prime
        """
        _is_valid_int(number)
        if number < 2:
            return False
        i = 2
        while i * i <= number:
            if number % i == 0:
                return False
            i += 1
        return True

    @staticmethod
    def is_square(number: int) -> bool:
        """
        Checking the number by square
        :param number: an integer to be entered for analysis
        :return: a boolean value of matching a number with a square
        """
        _is_valid_int(number)
        if number < 0:
            return False
        return (number ** 0.5) % 1 == 0


class NumeralSystem:
    @staticmethod
    def to_base(number: int,
                base: int, *,
                bits: int = 0) -> str:
        """
        Conversion from decimal to any other number system (from binary to thirty-six-bit)
        :param number: an integer to be entered for analysis
        :param base: an integer, the number of the number system from 2 to 36
        :param bits: optional integer number of bits, default -1 (disabled)
        :return: string, a number in the entered number system
        """
        _is_valid_int(number, base, bits)
        if not 2 <= base <= 36:
            raise ValueError('The base number system must be positive')
        elif bits < 0:
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
        return ('-' if negative else '') + result[::-1] if bits == 0 else \
            ('-' if negative else '') + (result + ('0' * (bits - len(result))))[:bits][::-1]


class PerformanceTracking:
    def __init__(self, *, expected: int = 60) -> None:
        """
        Initialization of the class, the beginning of the countdown
        :param expected: optional parameter of the expected program execution time
        """
        _is_valid_int(expected)
        self.start = perf_counter()
        self.expected = expected

    def __del__(self) -> None:
        """
        Object deletion, end of countdown
        :return: output to the console of the program's operation time from the beginning of class initialization
        """
        result = perf_counter() - self.start
        print('\nThe program was completed in \033[1m{}{}\033[0m second!'.format('\033[32m'
                                                                                 if result <= self.expected
                                                                                 else '\033[31m',
                                                                                 result))

    @staticmethod
    def func_timer(*, expected: int = 10) -> Any:
        """
        A decorated function for calculating the time of operation of the function
        :param expected: optional parameter of the expected time of operation of the function in seconds, 10 by default
        :return: a decorator that outputs the execution time of a function to the console, comparing it with the expected one
        """
        _is_valid_int(expected)

        def decorator(func: Callable) -> Any:
            @wraps(func)
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

    @staticmethod
    def get_size(*, expected: int = 512) -> Any:
        """
        A decorated function for determining RAM consumption.
        :param expected: optional parameter of the expected number of bytes occupied by the function, 64 by default
        :return: a decorator that outputs the RAM consumption of a function to the console, comparing it with the expected
        """
        _is_valid_int(expected)

        def decorator(func: Callable) -> Any:
            @wraps(func)
            def wrapper(*args, **kwargs) -> Any:
                call = func(*args, **kwargs)
                result = getsizeof(call)
                print('Function «{}» occupies \033[1m{}{}\033[0m bytes in RAM!\n'.format(func.__name__,
                                                                                         '\033[32m'
                                                                                         if result <= expected
                                                                                         else '\033[31m',
                                                                                         result))
                return call

            return wrapper

        return decorator
