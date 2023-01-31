"""
author: notjik
license: MIT License

copyright: (C) 2023 notjik
"""
from typing import Callable

__all__ = ['Sort',
           'Find']


class Sort:
    @staticmethod
    # TODO: Bubble sorting method (https://sortvisualizer.com/bubblesort/)
    # TODO: Метод сортировки пузырьком (https://sortvisualizer.com/bubblesort/)
    def bubble(array: list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str, *,
               reverse: bool = False,
               alg: Callable[[int | float | str | tuple | list, int | float | str | tuple | list], bool] =
               lambda x, y: x < y) \
            -> list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str:
        tp = type(array)
        if tp != list:
            array = list(array)
        for i in range(len(array) - 1):
            for j in range(len(array) - i - 1):
                if alg(array[j + 1], array[j]) if not reverse else alg(array[j], array[j + 1]):
                    array[j + 1], array[j] = array[j], array[j + 1]
        return ''.join(array) if tp == str else tp(array)

    @staticmethod
    # TODO: Shaker sorting method (https://sortvisualizer.com/shakersort/)
    # TODO: Метод сортировки шейкером (https://sortvisualizer.com/shakersort/)
    def shaker(array: list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str,
               reverse: bool = False,
               alg: Callable[[int | float | str | tuple | list, int | float | str | tuple | list], bool] =
               lambda x, y: x < y) \
            -> list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str:
        tp = type(array)
        if tp != list:
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
    # TODO: Insertion sorting method (https://sortvisualizer.com/insertionsort/)
    # TODO: Метод сортировки вставками (https://sortvisualizer.com/insertionsort/)
    def insertion(array: list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str, *,
                  reverse: bool = False,
                  alg: Callable[[int | float | str | tuple | list, int | float | str | tuple | list], bool] =
                  lambda x, y: x < y) \
            -> list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str:
        tp = type(array)
        if tp != list:
            array = list(array)
        for i in range(1, len(array)):
            x = array[i]
            j = i - 1
            while j >= 0 and alg(x, array[j]) if not reverse else alg(array[j], x):
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = x
        return ''.join(array) if tp == str else tp(array)

    @staticmethod
    # TODO: Selection sorting method (https://sortvisualizer.com/selectionsort/)
    # TODO: Метод сортировки выборкой (https://sortvisualizer.com/selectionsort/)
    def selection(array: list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str, *,
                  reverse: bool = False,
                  alg: Callable[[int | float | str | tuple | list, int | float | str | tuple | list], bool] =
                  lambda x, y: x < y) \
            -> list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str:
        tp = type(array)
        if tp != list:
            array = list(array)
        for i in range(len(array)):
            tmp = i
            for j in range(i + 1, len(array)):
                if alg(array[j], array[tmp]) if not reverse else alg(array[tmp], array[j]):
                    tmp = j
            array[i], array[tmp] = array[tmp], array[i]
        return ''.join(array) if tp == str else tp(array)

    @staticmethod
    # TODO: Counting sorting method (https://www.cs.usfca.edu/~galles/visualization/CountingSort.html)
    # TODO: Метод сортировки подсчётом (https://www.cs.usfca.edu/~galles/visualization/CountingSort.html)
    def counting(array: list[int | float] | tuple[int | float], *,
                 reverse: bool = False) -> list[int | float] | tuple[int | float]:
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
    # TODO: Merge sorting method (https://sortvisualizer.com/mergesort/)
    # TODO: Метод сортировки слиянием (https://sortvisualizer.com/mergesort/)
    def merge(array: list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str, *,
              reverse: bool = False,
              alg: Callable[[int | float | str | tuple | list, int | float | str | tuple | list], bool] =
              lambda x, y: x < y) \
            -> list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str:
        tp = type(array)
        if tp != list:
            array = list(array)
        if len(array) <= 1:
            median = len(array) // 2
            if not reverse:
                left, right = array[:median], array[median:]
            else:
                left, right = array[median:], array[:median]
            Sort.merge(array=left, reverse=reverse)
            Sort.merge(array=right, reverse=reverse)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if alg(left[i], right[j]):
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
    # TODO: Hoare's sorting method (https://sortvisualizer.com/quicksort/)
    # TODO: Метод сортировки Хоара (https://sortvisualizer.com/quicksort/)
    def quick(array: list[int | float | str | tuple | list] | tuple[int | float | str | tuple | list] | str,
              start: int = 0,
              end: int | None = None, *,
              reverse: bool = False,
              alg: Callable[[int | float | str | tuple | list, int | float | str | tuple | list], bool] =
              lambda x, y: x < y) \
            -> list[int | float | str] | tuple[int | float | str] | str:
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
        if tp != list:
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
    # TODO: Linear search
    # TODO: Линейный поиск
    def linear(array: list[int | float | str] | tuple[int | float | str] | str,
               element: int | float | str, *,
               reverse: bool = False) -> int | None:
        for i in range(len(array)) if not reverse else range(len(array) - 1, -1, -1):
            if array[i] == element:
                return i
        return None

    @staticmethod
    # TODO: Binary search (sorted collection)
    # TODO: Бинарный поиск (отсортированной коллекции)
    def binary(array: list[int | float | str] | tuple[int | float | str] | str,
               element: int | float | str,
               start: int = 0,
               end: int | None = None) -> int | None:
        if end is None:
            end = len(array) - 1
        i = None
        while (start <= end) and (i is None):
            median = (start + end) // 2
            if array[median] == element:
                i = median
            else:
                if element < array[median]:
                    end = median - 1
                else:
                    start = median + 1
        return i


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

    if type(array) != str:
        print('Counting:')
        print('Before: {}'.format(array))
        print('After: {}'.format(Sort.counting(array[:])))
        print('{} operations per {}\n'.format(operations, timeit('Sort.counting({})'.format(array[:]),
                                                                 'from __main__ import Sort', number=operations)))

    print('Merge:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.bubble(array[:])))
    print('{} operations per {}\n'.format(operations, timeit('Sort.merge({})'.format(array[:]) if type(array) != str
                                                             else 'Sort.merge("{}")'.format(array[:]),
                                                             'from __main__ import Sort', number=operations)))

    print('Quick:')
    print('Before: {}'.format(array))
    print('After: {}'.format(Sort.quick(array[:])))
    print('{} operations per {}'.format(operations, timeit('Sort.quick({})'.format(array[:]) if type(array) != str
                                                           else 'Sort.quick("{}")'.format(array[:]),
                                                           'from __main__ import Sort', number=operations)))
