"""
A module with customizable sorting and search algorithms.

-----

:author: notjik
:license: MIT License
:copyright: (c) 2023 notjik
"""
from typing import Callable

from ._validator import _is_valid_sequence, _is_valid_bool

__all__ = ['Sort',
           'Find']


class Sort:
    @staticmethod
    def bubble(array: list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str, *,
               reverse: bool = False,
               alg: Callable[[int | float | str | tuple | list, int | float | str | tuple | list], bool] =
               lambda x, y: x < y) \
            -> list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str:
        """
        Bubble sorting method (https://sortvisualizer.com/bubblesort/)
        :param array: a sequence of elements from the numbers or strings to be filled in, or the same sequences that need to be sorted
        :param reverse: optional boolean value to determine whether to perform reverse sorting
        :param alg: optional callable object that defines 2 variables and interacts with them to pass new logic for processing numbers
        :return: a sorted sequence based on the passed parameters
        """
        _is_valid_sequence(array)
        _is_valid_bool()
        tp = type(array)
        if not isinstance(array, list):
            array = list(array)
        for i in range(len(array) - 1):
            for j in range(len(array) - i - 1):
                if alg(array[j + 1], array[j]) if not reverse else alg(array[j], array[j + 1]):
                    array[j + 1], array[j] = array[j], array[j + 1]
        return ''.join(array) if tp == str else tp(array) if tp != set else list(array)

    @staticmethod
    def shaker(array: list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str,
               reverse: bool = False,
               alg: Callable[[int | float | str | tuple | list, int | float | str | tuple | list], bool] =
               lambda x, y: x < y) \
            -> list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str:
        """
        Shaker sorting method (https://sortvisualizer.com/shakersort/)
        :param array: a sequence of elements from the numbers or strings to be filled in, or the same sequences that need to be sorted
        :param reverse: optional boolean value to determine whether to perform reverse sorting
        :param alg: optional callable object that defines 2 variables and interacts with them to pass new logic for processing numbers
        :return: a sorted sequence based on the passed parameters
        """
        _is_valid_sequence(array)
        tp = type(array)
        if not isinstance(array, list):
            array = list(array)
        left, right = 0, len(array) - 1
        while left <= right:
            for i in range(right, left, -1):
                if alg(array[i], array[i - 1]) if not reverse else alg(array[i - 1], array[i]):
                    array[i - 1], array[i] = array[i], array[i - 1]
            left += 1
            for i in range(left, right):
                if alg(array[i + 1], array[i]) if not reverse else alg(array[i], array[i + 1]):
                    array[i], array[i + 1] = array[i + 1], array[i]
            right -= 1
        return ''.join(array) if tp == str else tp(array)

    @staticmethod
    def insertion(array: list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str, *,
                  reverse: bool = False,
                  alg: Callable[[int | float | str | tuple | list, int | float | str | tuple | list], bool] =
                  lambda x, y: x < y) \
            -> list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str:
        """
        Insertion sorting method (https://sortvisualizer.com/insertionsort/)
        :param array: a sequence of elements from the numbers or strings to be filled in, or the same sequences that need to be sorted
        :param reverse: optional boolean value to determine whether to perform reverse sorting
        :param alg: optional callable object that defines 2 variables and interacts with them to pass new logic for processing numbers
        :return: a sorted sequence based on the passed parameters
        """
        _is_valid_sequence(array)
        tp = type(array)
        if not isinstance(array, list):
            if isinstance(array, dict):
                raise ValueError('Dictionary is an invalid type for sorting')
            array = list(array)
        for i in range(1, len(array)):
            x = array[i]
            j = i - 1
            while j >= 0 and alg(x, array[j]) if not reverse else j >= 0 and alg(array[j], x):
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = x
        return ''.join(array) if tp == str else tp(array)

    @staticmethod
    def selection(array: list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str, *,
                  reverse: bool = False,
                  alg: Callable[[int | float | str | tuple | list, int | float | str | tuple | list], bool] =
                  lambda x, y: x < y) \
            -> list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str:
        """
        Selection sorting method (https://sortvisualizer.com/selectionsort/)
        :param array: a sequence of elements from the numbers or strings to be filled in, or the same sequences that need to be sorted
        :param reverse: optional boolean value to determine whether to perform reverse sorting
        :param alg: optional callable object that defines 2 variables and interacts with them to pass new logic for processing numbers
        :return: a sorted sequence based on the passed parameters
        """
        _is_valid_sequence(array)
        tp = type(array)
        if not isinstance(array, list):
            if isinstance(array, dict):
                raise ValueError('Dictionary is an invalid type for sorting')
            array = list(array)
        for i in range(len(array)):
            tmp = i
            for j in range(i + 1, len(array)):
                if alg(array[j], array[tmp]) if not reverse else alg(array[tmp], array[j]):
                    tmp = j
            array[i], array[tmp] = array[tmp], array[i]
        return ''.join(array) if tp == str else tp(array)

    @staticmethod
    def counting(array: list[int | float] | tuple[int | float], *,
                 reverse: bool = False) -> list[int | float] | tuple[int | float]:
        """
        Counting sorting method (https://www.cs.usfca.edu/~galles/visualization/CountingSort.html)
        :param array: a sequence of elements from the compared numbers that need to be sorted
        :param reverse: optional boolean value to determine whether to perform reverse sorting
        :return: a sorted sequence based on passed parameters
        """
        _is_valid_sequence(array, closed=[str])
        tp = type(array)
        array_init = [0] * (max(array) + 1)
        result = []
        for i in range(len(array)):
            array_init[array[i]] += 1
        for i in range(len(array_init)) if not reverse else range(len(array_init) - 1, -1, -1):
            if array_init[i]:
                for k in range(array_init[i]):
                    result.append(i)
        return tp(result)

    @staticmethod
    def merge(array: list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str, *,
              reverse: bool = False,
              alg: Callable[[int | float | str | tuple | list, int | float | str | tuple | list], bool] =
              lambda x, y: x < y) \
            -> list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str:
        """
        Merge sorting method (https://sortvisualizer.com/mergesort/)
        :param array: a sequence of elements from the numbers or strings to be filled in, or the same sequences that need to be sorted
        :param reverse: optional boolean value to determine whether to perform reverse sorting
        :param alg: optional callable object that defines 2 variables and interacts with them to pass new logic for processing numbers
        :return: a sorted sequence based on the passed parameters
        """
        _is_valid_sequence(array)
        tp = type(array)
        if not isinstance(array, list):
            if isinstance(array, dict):
                raise ValueError('Dictionary is an invalid type for sorting')
            array = list(array)
        if len(array) > 1:
            median = len(array) // 2
            left, right = array[:median], array[median:]
            Sort.merge(array=left, reverse=reverse, alg=alg)
            Sort.merge(array=right, reverse=reverse, alg=alg)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if alg(left[i], right[j]) if not reverse else alg(right[j], left[i]):
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
        return ''.join(array) if tp == str else tp(array)

    @staticmethod
    def quick(array: list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str,
              start: int = 0,
              end: int | None = None, *,
              reverse: bool = False,
              alg: Callable[[int | float | str | tuple | list, int | float | str | tuple | list], bool] =
              lambda x, y: x < y) \
            -> list[int | float | str] | tuple[int | float | str] | str:
        """
        Hoare's sorting method — Quicksort (https://sortvisualizer.com/quicksort/)
        :param array: a sequence of elements from the numbers or strings to be filled in, or the same sequences that need to be sorted
        :param start: an optional integer, the value from which to start sorting
        :param end: optional integer, the value on which to end the sorting
        :param reverse: optional boolean value to determine whether to perform reverse sorting
        :param alg: optional callable object that defines 2 variables and interacts with them to pass new logic for processing numbers
        :return: a sorted sequence based on the passed parameters
        """
        _is_valid_sequence(array)

        def partition(array: list,
                      start: int,
                      end: int):
            pivot = start
            for i in range(start + 1, end + 1):
                if alg(array[i], array[start]) if not reverse else alg(array[start], array[i]):
                    pivot += 1
                    array[i], array[pivot] = array[pivot], array[i]
            array[pivot], array[start] = array[start], array[pivot]
            return pivot

        tp = type(array)
        if not isinstance(array, list):
            if isinstance(array, dict):
                raise ValueError('Dictionary is an invalid type for sorting')
            array = list(array)
        if end is None:
            end = len(array) - 1
        if start >= end:
            return []
        pivot = partition(array, start, end)
        Sort.quick(array=array, start=start, end=pivot - 1, alg=alg, reverse=reverse)
        Sort.quick(array=array, start=pivot + 1, end=end, alg=alg, reverse=reverse)
        return ''.join(array) if tp == str else tp(array)


class Find:
    @staticmethod
    def linear(array: list[int | float | str | list | tuple] | tuple[int | float | str | list | tuple] | str,
               element: int | float | complex | str | list | tuple, *,
               reverse: bool = False) -> int:
        """
        Linear search
        :param array: the sequence in which you need to find the desired element
        :param element: a number, symbol, or sequence whose index needs to be found
        :param reverse: optional boolean value if you need to find the character from the end
        :return: an integer of the index of occurrence of the desired value, if the number is not found, -1 is output
        """
        _is_valid_sequence(array)
        for i in range(len(array)) if not reverse else range(len(array) - 1, -1, -1):
            if array[i] == element:
                return i
        return -1

    @staticmethod
    def binary(array: list[int | float | str | list | tuple] | tuple[int | float | str | list | tuple] | str,
               element: int | float | str | list | tuple,
               start: int = 0,
               end: int | None = None) -> int | None:
        """
        Binary search (sorted sequence)
        :param array: the SORTED sequence in which you need to find the element
        :param element: a number being compared, symbol or sequence whose index needs to be found
        :param start: optional integer, the value to start the search with
        :param end: optional integer, the value on which to end the search
        :return: an integer of the index of the appearance of the desired value or the one on which it will have to stand
        """
        _is_valid_sequence(array)
        if end is None:
            end = len(array) - 1
        result = 0
        while start <= end:
            median = (start + end) // 2
            if array[median] == element:
                result = median
                break
            elif element < array[median]:
                end = median - 1
                result = median
            else:
                start = median + 1
                result = start
        return result


if __name__ == '__main__':
    from timeit import timeit
    from random import randint

    l: int = 10
    array: list[int] = [randint(0, 1000) for r in range(l)]
    operations: int = 100

    print('Bubble:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.bubble(array[:])))
    print('{} operations per {}\n'.format(operations, timeit('Sort.bubble({})'.format(array[:]) if type(array) != str
                                                             else 'Sort.bubble("{}")'.format(array[:]),
                                                             'from __main__ import Sort', number=operations)))

    print('Shaker:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.shaker(array[:])))
    print('{} operations per {}\n'.format(operations, timeit('Sort.shaker({})'.format(array[:]) if type(array) != str
                                                             else 'Sort.shaker("{}")'.format(array[:]),
                                                             'from __main__ import Sort', number=operations)))

    print('Insertion:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.insertion(array[:])))
    print('{} operations per {}\n'.format(operations, timeit('Sort.insertion({})'.format(array[:]) if type(array) != str
                                                             else 'Sort.insertion("{}")'.format(array[:]),
                                                             'from __main__ import Sort', number=operations)))

    print('Selection:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.selection(array[:])))
    print('{} operations per {}\n'.format(operations, timeit('Sort.selection({})'.format(array[:]) if type(array) != str
                                                             else 'Sort.selection("{}")'.format(array[:]),
                                                             'from __main__ import Sort', number=operations)))

    if not isinstance(array, str):
        print('Counting:')
        print('Before: {}'.format(array))
        print('After: {}'.format(Sort.counting(array[:])))
        print('{} operations per {}\n'.format(operations, timeit('Sort.counting({})'.format(array[:]),
                                                                 'from __main__ import Sort', number=operations)))

    print('Merge:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.merge(array[:])))
    print('{} operations per {}\n'.format(operations, timeit('Sort.merge({})'.format(array[:]) if type(array) != str
                                                             else 'Sort.merge("{}")'.format(array[:]),
                                                             'from __main__ import Sort', number=operations)))

    print('Quick:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.quick(array[:])))
    print('{} operations per {}'.format(operations, timeit('Sort.quick({})'.format(array[:]) if type(array) != str
                                                           else 'Sort.quick("{}")'.format(array[:]),
                                                           'from __main__ import Sort', number=operations)))
