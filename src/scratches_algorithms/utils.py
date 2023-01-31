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
    # TODO: Search for all divisors
    # TODO: Поиск всех делителей
    def divisors(number: int, *, nontrivial: bool = False) -> list:
        result = []
        i = 1 if not nontrivial else 2
        while i ** 2 <= number:
            if i ** 2 == number:
                result.append(i)
            elif number % i == 0:
                result += [i, number // i]
            i += 1
        return result

    @staticmethod
    # TODO: Finding the n-th term of the Fibonacci number
    # TODO: Нахождение n-го члена числа Фибоначчи
    def fibonacci(number: int) -> int:
        return round((((1 + 5 ** 0.5) / 2) ** number - ((1 - 5 ** 0.5) / 2) ** number) / 5 ** 0.5)

    @staticmethod
    # TODO: Checking a number for prime
    # TODO: Проверка числа на простоту
    def is_prime(number: int) -> bool:
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
    def is_square(n: int) -> bool:
        return (n ** 0.5) % 1 == 0


class NumeralSystem:
    @staticmethod
    # TODO: Conversion from decimal to any other number system (up to 36)
    # TODO: Перевод из десятичной системы счисления в любую другую (до 36)
    def to_base(number: int, base: int, *, bit=None) -> str:
        alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
        result = alphabet[number % base]
        while number >= base:
            number //= base
            result += alphabet[number % base]
        return result[::-1] if bit is None else (result + ('0' * (bit - len(result))))[:bit][::-1]


class PerformanceTracking:
    # TODO: Initialization of the class, the beginning of the countdown
    # TODO: Инициализация класса, начало отсчёта
    def __init__(self) -> None:
        self.start = perf_counter()

    # TODO: Object deletion, end of countdown
    # TODO: Удаление объекта, окончание отсчёта
    def __del__(self) -> None:
        print('\nThe program was completed in {} second!'.format(perf_counter() - self.start))

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
                                                                                           '\033[32m' if result < expected
                                                                                           else '\033[31m',
                                                                                           result))
                return call

            return wrapper

        return decorator
