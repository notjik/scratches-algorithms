from time import time


class DivFunc:
    @staticmethod
    # TODO: Search for all divisors
    # TODO: Поиск всех делителей
    def divisor(x: int) -> list:
        a = []
        i = 1
        while i ** 2 <= x:
            if i ** 2 == x:
                a.append(i)
            elif x % i == 0:
                a += [i, x // i]
            i += 1
        a.sort()
        return a

    @staticmethod
    # TODO: Finding nontrivial divisors
    # TODO: Поиск нетривиальных делителей
    def nontrivial_divisor(x: int) -> list:
        a = []
        i = 2
        while i ** 2 <= x:
            if i ** 2 == x:
                a.append(i)
            elif x % i == 0:
                a += [i, x // i]
            i += 1
        a.sort()
        return a

    @staticmethod
    # TODO: Checking a number for simplicity
    # TODO: Проверка числа на простоту
    def is_prime(n: int) -> bool:
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    # TODO: Checking the number by square
    # TODO: Проверка числа на квадрат
    def is_square(n: int) -> bool:
        return (n ** 0.5) % 1 == 0


class NumeralSystem:
    @staticmethod
    # TODO: Transfer to another number system
    # TODO: Перевод в другую систему счисления
    def to_base(number: int, base: int) -> str:
        alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
        result = alphabet[number % base]
        while number >= base:
            number //= base
            result += alphabet[number % base]
        return result[::-1]


class PerformanceTracking:
    # TODO: Initialization of the class, the beginning of the countdown
    # TODO: Инициализация класса, начало отсчёта
    def __init__(self) -> None:
        self.start = time()

    # TODO: Object deletion, end of countdown
    # TODO: Удаление объекта, окончание отсчёта
    def __del__(self) -> None:
        print('\nThe program was completed in {} second!'.format(time() - self.start))
