from unittest import TestCase
from src.scratches_algorithms import algorithms


class TestBubbleSort(TestCase):
    def test_equal(self):
        self.assertEqual(algorithms.Sort.bubble([0, 1, 2, 3]),
                         [0, 1, 2, 3])
        self.assertEqual(algorithms.Sort.bubble([1, 3, 2, 0]),
                         [0, 1, 2, 3])
        self.assertEqual(algorithms.Sort.bubble([0, 1, 2, 3],
                                                reverse=True),
                         [3, 2, 1, 0])
        self.assertEqual(algorithms.Sort.bubble([1, 3, 2, 0],
                                                reverse=True),
                         [3, 2, 1, 0])
        self.assertEqual(algorithms.Sort.bubble([0, 1, 2, 3],
                                                alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [0, 2, 1, 3])
        self.assertEqual(algorithms.Sort.bubble([1, 3, 2, 0],
                                                alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [0, 2, 1, 3])
        self.assertEqual(algorithms.Sort.bubble([0, 1, 2, 3],
                                                reverse=True,
                                                alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [3, 1, 2, 0])
        self.assertEqual(algorithms.Sort.bubble([1, 3, 2, 0],
                                                reverse=True,
                                                alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [3, 1, 2, 0])
        self.assertEqual(algorithms.Sort.bubble(['a', 'b', 'c', 'd']),
                         ['a', 'b', 'c', 'd'])
        self.assertEqual(algorithms.Sort.bubble(['c', 'd', 'b', 'a']),
                         ['a', 'b', 'c', 'd'])
        self.assertEqual(algorithms.Sort.bubble(['a', 'b', 'c', 'd'],
                                                reverse=True),
                         ['d', 'c', 'b', 'a'])
        self.assertEqual(algorithms.Sort.bubble(['c', 'd', 'b', 'a'],
                                                reverse=True),
                         ['d', 'c', 'b', 'a'])
        self.assertEqual(algorithms.Sort.bubble(['a', 'B', 'c', 'D'],
                                                alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['B', 'D', 'a', 'c'])
        self.assertEqual(algorithms.Sort.bubble(['c', 'D', 'B', 'a'],
                                                alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['B', 'D', 'a', 'c'])
        self.assertEqual(algorithms.Sort.bubble(['a', 'B', 'c', 'D'],
                                                reverse=True,
                                                alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['c', 'a', 'D', 'B'])
        self.assertEqual(algorithms.Sort.bubble(['c', 'D', 'B', 'a'],
                                                reverse=True,
                                                alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['c', 'a', 'D', 'B'])
        self.assertEqual(algorithms.Sort.bubble([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]]),
                         [[0, 0], [0, 1, 2, 3], [0, 2, 3], [99]])
        self.assertEqual(algorithms.Sort.bubble([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                                reverse=True),
                         [[99], [0, 2, 3], [0, 1, 2, 3], [0, 0]])
        self.assertEqual(algorithms.Sort.bubble([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                                alg=lambda x, y: sum(x) < sum(y)),
                         [[0, 0], [0, 2, 3], [0, 1, 2, 3], [99]])
        self.assertEqual(algorithms.Sort.bubble([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                                reverse=True,
                                                alg=lambda x, y: sum(x) < sum(y)),
                         [[99], [0, 1, 2, 3], [0, 2, 3], [0, 0]])

    def test_raises(self):
        self.assertRaises(TypeError,
                          algorithms.Sort.bubble)
        self.assertRaises(TypeError,
                          algorithms.Sort.bubble,
                          100)
        self.assertRaises(TypeError,
                          algorithms.Sort.bubble,
                          [0, 1, 2, 3],
                          alg=lambda x: x[0])
        self.assertRaises(ValueError,
                          algorithms.Sort.bubble,
                          {'key': 'value'})


class TestShakerSort(TestCase):
    def test_equal(self):
        self.assertEqual(algorithms.Sort.shaker([0, 1, 2, 3]),
                         [0, 1, 2, 3])
        self.assertEqual(algorithms.Sort.shaker([1, 3, 2, 0]),
                         [0, 1, 2, 3])
        self.assertEqual(algorithms.Sort.shaker([0, 1, 2, 3],
                                                reverse=True),
                         [3, 2, 1, 0])
        self.assertEqual(algorithms.Sort.shaker([1, 3, 2, 0],
                                                reverse=True),
                         [3, 2, 1, 0])
        self.assertEqual(algorithms.Sort.shaker([0, 1, 2, 3],
                                                alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [0, 2, 1, 3])
        self.assertEqual(algorithms.Sort.shaker([1, 3, 2, 0],
                                                alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [0, 2, 1, 3])
        self.assertEqual(algorithms.Sort.shaker([0, 1, 2, 3],
                                                reverse=True,
                                                alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [3, 1, 2, 0])
        self.assertEqual(algorithms.Sort.shaker([1, 3, 2, 0],
                                                reverse=True,
                                                alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [3, 1, 2, 0])
        self.assertEqual(algorithms.Sort.shaker(['a', 'b', 'c', 'd']),
                         ['a', 'b', 'c', 'd'])
        self.assertEqual(algorithms.Sort.shaker(['c', 'd', 'b', 'a']),
                         ['a', 'b', 'c', 'd'])
        self.assertEqual(algorithms.Sort.shaker(['a', 'b', 'c', 'd'],
                                                reverse=True),
                         ['d', 'c', 'b', 'a'])
        self.assertEqual(algorithms.Sort.shaker(['c', 'd', 'b', 'a'],
                                                reverse=True),
                         ['d', 'c', 'b', 'a'])
        self.assertEqual(algorithms.Sort.shaker(['a', 'B', 'c', 'D'],
                                                alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['B', 'D', 'a', 'c'])
        self.assertEqual(algorithms.Sort.shaker(['c', 'D', 'B', 'a'],
                                                alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['B', 'D', 'a', 'c'])
        self.assertEqual(algorithms.Sort.shaker(['a', 'B', 'c', 'D'],
                                                reverse=True,
                                                alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['c', 'a', 'D', 'B'])
        self.assertEqual(algorithms.Sort.shaker(['c', 'D', 'B', 'a'],
                                                reverse=True,
                                                alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['c', 'a', 'D', 'B'])
        self.assertEqual(algorithms.Sort.shaker([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]]),
                         [[0, 0], [0, 1, 2, 3], [0, 2, 3], [99]])
        self.assertEqual(algorithms.Sort.shaker([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                                reverse=True),
                         [[99], [0, 2, 3], [0, 1, 2, 3], [0, 0]])
        self.assertEqual(algorithms.Sort.shaker([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                                alg=lambda x, y: sum(x) < sum(y)),
                         [[0, 0], [0, 2, 3], [0, 1, 2, 3], [99]])
        self.assertEqual(algorithms.Sort.shaker([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                                reverse=True,
                                                alg=lambda x, y: sum(x) < sum(y)),
                         [[99], [0, 1, 2, 3], [0, 2, 3], [0, 0]])

    def test_raises(self):
        self.assertRaises(TypeError,
                          algorithms.Sort.shaker)
        self.assertRaises(TypeError,
                          algorithms.Sort.shaker,
                          100)
        self.assertRaises(TypeError,
                          algorithms.Sort.shaker,
                          [0, 1, 2, 3],
                          alg=lambda x: x[0])
        self.assertRaises(ValueError,
                          algorithms.Sort.shaker,
                          {'key': 'value'})


class TestInsertionSort(TestCase):
    def test_equal(self):
        self.assertEqual(algorithms.Sort.insertion([0, 1, 2, 3]),
                         [0, 1, 2, 3])
        self.assertEqual(algorithms.Sort.insertion([1, 3, 2, 0]),
                         [0, 1, 2, 3])
        self.assertEqual(algorithms.Sort.insertion([0, 1, 2, 3],
                                                   reverse=True),
                         [3, 2, 1, 0])
        self.assertEqual(algorithms.Sort.insertion([1, 3, 2, 0],
                                                   reverse=True),
                         [3, 2, 1, 0])
        self.assertEqual(algorithms.Sort.insertion([0, 1, 2, 3],
                                                   alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [0, 2, 1, 3])
        self.assertEqual(algorithms.Sort.insertion([1, 3, 2, 0],
                                                   alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [0, 2, 1, 3])
        self.assertEqual(algorithms.Sort.insertion([0, 1, 2, 3],
                                                   reverse=True,
                                                   alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [3, 1, 2, 0])
        self.assertEqual(algorithms.Sort.insertion([1, 3, 2, 0],
                                                   reverse=True,
                                                   alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [3, 1, 2, 0])
        self.assertEqual(algorithms.Sort.insertion(['a', 'b', 'c', 'd']),
                         ['a', 'b', 'c', 'd'])
        self.assertEqual(algorithms.Sort.insertion(['c', 'd', 'b', 'a']),
                         ['a', 'b', 'c', 'd'])
        self.assertEqual(algorithms.Sort.insertion(['a', 'b', 'c', 'd'],
                                                   reverse=True),
                         ['d', 'c', 'b', 'a'])
        self.assertEqual(algorithms.Sort.insertion(['c', 'd', 'b', 'a'],
                                                   reverse=True),
                         ['d', 'c', 'b', 'a'])
        self.assertEqual(algorithms.Sort.insertion(['a', 'B', 'c', 'D'],
                                                   alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['B', 'D', 'a', 'c'])
        self.assertEqual(algorithms.Sort.insertion(['c', 'D', 'B', 'a'],
                                                   alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['B', 'D', 'a', 'c'])
        self.assertEqual(algorithms.Sort.insertion(['a', 'B', 'c', 'D'],
                                                   reverse=True,
                                                   alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['c', 'a', 'D', 'B'])
        self.assertEqual(algorithms.Sort.insertion(['c', 'D', 'B', 'a'],
                                                   reverse=True,
                                                   alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['c', 'a', 'D', 'B'])
        self.assertEqual(algorithms.Sort.insertion([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]]),
                         [[0, 0], [0, 1, 2, 3], [0, 2, 3], [99]])
        self.assertEqual(algorithms.Sort.insertion([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                                   reverse=True),
                         [[99], [0, 2, 3], [0, 1, 2, 3], [0, 0]])
        self.assertEqual(algorithms.Sort.insertion([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                                   alg=lambda x, y: sum(x) < sum(y)),
                         [[0, 0], [0, 2, 3], [0, 1, 2, 3], [99]])
        self.assertEqual(algorithms.Sort.insertion([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                                   reverse=True,
                                                   alg=lambda x, y: sum(x) < sum(y)),
                         [[99], [0, 1, 2, 3], [0, 2, 3], [0, 0]])

    def test_raises(self):
        self.assertRaises(TypeError, algorithms.Sort.insertion)
        self.assertRaises(TypeError, algorithms.Sort.insertion, 100)
        self.assertRaises(TypeError, algorithms.Sort.insertion, [0, 1, 2, 3], alg=lambda x: x[0])
        self.assertRaises(ValueError, algorithms.Sort.insertion, {'key': 'value'})


class TestSelectionSort(TestCase):
    def test_equal(self):
        self.assertEqual(algorithms.Sort.selection([0, 1, 2, 3]),
                         [0, 1, 2, 3])
        self.assertEqual(algorithms.Sort.selection([1, 3, 2, 0]),
                         [0, 1, 2, 3])
        self.assertEqual(algorithms.Sort.selection([0, 1, 2, 3],
                                                   reverse=True),
                         [3, 2, 1, 0])
        self.assertEqual(algorithms.Sort.selection([1, 3, 2, 0],
                                                   reverse=True),
                         [3, 2, 1, 0])
        self.assertEqual(algorithms.Sort.selection([0, 1, 2, 3],
                                                   alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [0, 2, 1, 3])
        self.assertEqual(algorithms.Sort.selection([1, 3, 2, 0],
                                                   alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [0, 2, 1, 3])
        self.assertEqual(algorithms.Sort.selection([0, 1, 2, 3],
                                                   reverse=True,
                                                   alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [3, 1, 2, 0])
        self.assertEqual(algorithms.Sort.selection([1, 3, 2, 0],
                                                   reverse=True,
                                                   alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [3, 1, 2, 0])
        self.assertEqual(algorithms.Sort.selection(['a', 'b', 'c', 'd']),
                         ['a', 'b', 'c', 'd'])
        self.assertEqual(algorithms.Sort.selection(['c', 'd', 'b', 'a']),
                         ['a', 'b', 'c', 'd'])
        self.assertEqual(algorithms.Sort.selection(['a', 'b', 'c', 'd'],
                                                   reverse=True),
                         ['d', 'c', 'b', 'a'])
        self.assertEqual(algorithms.Sort.selection(['c', 'd', 'b', 'a'],
                                                   reverse=True),
                         ['d', 'c', 'b', 'a'])
        self.assertEqual(algorithms.Sort.selection(['a', 'B', 'c', 'D'],
                                                   alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['B', 'D', 'a', 'c'])
        self.assertEqual(algorithms.Sort.selection(['c', 'D', 'B', 'a'],
                                                   alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['B', 'D', 'a', 'c'])
        self.assertEqual(algorithms.Sort.selection(['a', 'B', 'c', 'D'],
                                                   reverse=True,
                                                   alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['c', 'a', 'D', 'B'])
        self.assertEqual(algorithms.Sort.selection(['c', 'D', 'B', 'a'],
                                                   reverse=True,
                                                   alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['c', 'a', 'D', 'B'])
        self.assertEqual(algorithms.Sort.selection([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]]),
                         [[0, 0], [0, 1, 2, 3], [0, 2, 3], [99]])
        self.assertEqual(algorithms.Sort.selection([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                                   reverse=True),
                         [[99], [0, 2, 3], [0, 1, 2, 3], [0, 0]])
        self.assertEqual(algorithms.Sort.selection([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                                   alg=lambda x, y: sum(x) < sum(y)),
                         [[0, 0], [0, 2, 3], [0, 1, 2, 3], [99]])
        self.assertEqual(algorithms.Sort.selection([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                                   reverse=True,
                                                   alg=lambda x, y: sum(x) < sum(y)),
                         [[99], [0, 1, 2, 3], [0, 2, 3], [0, 0]])

    def test_raises(self):
        self.assertRaises(TypeError,
                          algorithms.Sort.selection)
        self.assertRaises(TypeError,
                          algorithms.Sort.selection,
                          100)
        self.assertRaises(TypeError,
                          algorithms.Sort.selection,
                          [0, 1, 2, 3],
                          alg=lambda x: x[0])
        self.assertRaises(ValueError,
                          algorithms.Sort.selection,
                          {'key': 'value'})


class TestCountingSort(TestCase):
    def test_equal(self):
        self.assertEqual(algorithms.Sort.counting([0, 1, 2, 3]),
                         [0, 1, 2, 3])
        self.assertEqual(algorithms.Sort.counting([1, 3, 2, 0]),
                         [0, 1, 2, 3])
        self.assertEqual(algorithms.Sort.counting([0, 1, 2, 3],
                                                  reverse=True),
                         [3, 2, 1, 0])
        self.assertEqual(algorithms.Sort.counting([1, 3, 2, 0],
                                                  reverse=True),
                         [3, 2, 1, 0])

    def test_raises(self):
        self.assertRaises(TypeError,
                          algorithms.Sort.counting)
        self.assertRaises(TypeError,
                          algorithms.Sort.counting,
                          100)
        self.assertRaises(TypeError,
                          algorithms.Sort.counting,
                          [0, 1, 2, 3],
                          alg=lambda x: x[0])
        self.assertRaises(TypeError,
                          algorithms.Sort.counting,
                          {'key': 'value'})
        self.assertRaises(TypeError,
                          algorithms.Sort.counting,
                          ['c', 'd', 'b', 'a'])
        self.assertRaises(TypeError,
                          algorithms.Sort.counting,
                          [[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]])


class TestMergeSort(TestCase):
    def test_equal(self):
        self.assertEqual(algorithms.Sort.merge([0, 1, 2, 3]),
                         [0, 1, 2, 3])
        self.assertEqual(algorithms.Sort.merge([1, 3, 2, 0]),
                         [0, 1, 2, 3])
        self.assertEqual(algorithms.Sort.merge([0, 1, 2, 3],
                                               reverse=True),
                         [3, 2, 1, 0])
        self.assertEqual(algorithms.Sort.merge([1, 3, 2, 0],
                                               reverse=True),
                         [3, 2, 1, 0])
        self.assertEqual(algorithms.Sort.merge([0, 1, 2, 3],
                                               alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [0, 2, 1, 3])
        self.assertEqual(algorithms.Sort.merge([1, 3, 2, 0],
                                               alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [0, 2, 1, 3])
        self.assertEqual(algorithms.Sort.merge([0, 1, 2, 3],
                                               reverse=True,
                                               alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [3, 1, 2, 0])
        self.assertEqual(algorithms.Sort.merge([1, 3, 2, 0],
                                               reverse=True,
                                               alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [3, 1, 2, 0])
        self.assertEqual(algorithms.Sort.merge(['a', 'b', 'c', 'd']),
                         ['a', 'b', 'c', 'd'])
        self.assertEqual(algorithms.Sort.merge(['c', 'd', 'b', 'a']),
                         ['a', 'b', 'c', 'd'])
        self.assertEqual(algorithms.Sort.merge(['a', 'b', 'c', 'd'],
                                               reverse=True),
                         ['d', 'c', 'b', 'a'])
        self.assertEqual(algorithms.Sort.merge(['c', 'd', 'b', 'a'],
                                               reverse=True),
                         ['d', 'c', 'b', 'a'])
        self.assertEqual(algorithms.Sort.merge(['a', 'B', 'c', 'D'],
                                               alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['B', 'D', 'a', 'c'])
        self.assertEqual(algorithms.Sort.merge(['c', 'D', 'B', 'a'],
                                               alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['B', 'D', 'a', 'c'])
        self.assertEqual(algorithms.Sort.merge(['a', 'B', 'c', 'D'],
                                               reverse=True,
                                               alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['c', 'a', 'D', 'B'])
        self.assertEqual(algorithms.Sort.merge(['c', 'D', 'B', 'a'],
                                               reverse=True,
                                               alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['c', 'a', 'D', 'B'])
        self.assertEqual(algorithms.Sort.merge([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]]),
                         [[0, 0], [0, 1, 2, 3], [0, 2, 3], [99]])
        self.assertEqual(algorithms.Sort.merge([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                               reverse=True),
                         [[99], [0, 2, 3], [0, 1, 2, 3], [0, 0]])
        self.assertEqual(algorithms.Sort.merge([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                               alg=lambda x, y: sum(x) < sum(y)),
                         [[0, 0], [0, 2, 3], [0, 1, 2, 3], [99]])
        self.assertEqual(algorithms.Sort.merge([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                               reverse=True,
                                               alg=lambda x, y: sum(x) < sum(y)),
                         [[99], [0, 1, 2, 3], [0, 2, 3], [0, 0]])

    def test_raises(self):
        self.assertRaises(TypeError,
                          algorithms.Sort.merge)
        self.assertRaises(TypeError,
                          algorithms.Sort.merge,
                          100)
        self.assertRaises(TypeError,
                          algorithms.Sort.merge,
                          [0, 1, 2, 3],
                          alg=lambda x: x[0])
        self.assertRaises(ValueError,
                          algorithms.Sort.merge,
                          {'key': 'value'})


class TestQuickSort(TestCase):
    def test_equal(self):
        self.assertEqual(algorithms.Sort.quick([0, 1, 2, 3]),
                         [0, 1, 2, 3])
        self.assertEqual(algorithms.Sort.quick([1, 3, 2, 0]),
                         [0, 1, 2, 3])
        self.assertEqual(algorithms.Sort.quick([0, 1, 2, 3],
                                               reverse=True),
                         [3, 2, 1, 0])
        self.assertEqual(algorithms.Sort.quick([1, 3, 2, 0],
                                               reverse=True),
                         [3, 2, 1, 0])
        self.assertEqual(algorithms.Sort.quick([0, 1, 2, 3],
                                               alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [0, 2, 1, 3])
        self.assertEqual(algorithms.Sort.quick([1, 3, 2, 0],
                                               alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [0, 2, 1, 3])
        self.assertEqual(algorithms.Sort.quick([0, 1, 2, 3],
                                               reverse=True,
                                               alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [3, 1, 2, 0])
        self.assertEqual(algorithms.Sort.quick([1, 3, 2, 0],
                                               reverse=True,
                                               alg=lambda x, y: x % 2 < y % 2 or x % 2 == y % 2 and x < y),
                         [3, 1, 2, 0])
        self.assertEqual(algorithms.Sort.quick(['a', 'b', 'c', 'd']),
                         ['a', 'b', 'c', 'd'])
        self.assertEqual(algorithms.Sort.quick(['c', 'd', 'b', 'a']),
                         ['a', 'b', 'c', 'd'])
        self.assertEqual(algorithms.Sort.quick(['a', 'b', 'c', 'd'],
                                               reverse=True),
                         ['d', 'c', 'b', 'a'])
        self.assertEqual(algorithms.Sort.quick(['c', 'd', 'b', 'a'],
                                               reverse=True),
                         ['d', 'c', 'b', 'a'])
        self.assertEqual(algorithms.Sort.quick(['a', 'B', 'c', 'D'],
                                               alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['B', 'D', 'a', 'c'])
        self.assertEqual(algorithms.Sort.quick(['c', 'D', 'B', 'a'],
                                               alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['B', 'D', 'a', 'c'])
        self.assertEqual(algorithms.Sort.quick(['a', 'B', 'c', 'D'],
                                               reverse=True,
                                               alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['c', 'a', 'D', 'B'])
        self.assertEqual(algorithms.Sort.quick(['c', 'D', 'B', 'a'],
                                               reverse=True,
                                               alg=lambda x, y: ord(x) - ord('A') < ord(y) - ord('A')),
                         ['c', 'a', 'D', 'B'])
        self.assertEqual(algorithms.Sort.quick([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]]),
                         [[0, 0], [0, 1, 2, 3], [0, 2, 3], [99]])
        self.assertEqual(algorithms.Sort.quick([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                               reverse=True),
                         [[99], [0, 2, 3], [0, 1, 2, 3], [0, 0]])
        self.assertEqual(algorithms.Sort.quick([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                               alg=lambda x, y: sum(x) < sum(y)),
                         [[0, 0], [0, 2, 3], [0, 1, 2, 3], [99]])
        self.assertEqual(algorithms.Sort.quick([[0, 1, 2, 3], [0, 2, 3], [0, 0], [99]],
                                               reverse=True,
                                               alg=lambda x, y: sum(x) < sum(y)),
                         [[99], [0, 1, 2, 3], [0, 2, 3], [0, 0]])

    def test_raises(self):
        self.assertRaises(TypeError,
                          algorithms.Sort.quick)
        self.assertRaises(TypeError,
                          algorithms.Sort.quick,
                          100)
        self.assertRaises(TypeError,
                          algorithms.Sort.quick,
                          [0, 1, 2, 3],
                          alg=lambda x: x[0])
        self.assertRaises(ValueError,
                          algorithms.Sort.quick,
                          {'key': 'value'})


class TestLinearFind(TestCase):
    def test_equal(self):
        self.assertEqual(algorithms.Find.linear([1, 2, 3, 4, 5, 6],
                                                3),
                         2)
        self.assertEqual(algorithms.Find.linear([6, 2, 1, 3, 4, 8],
                                                3),
                         3)
        self.assertEqual(algorithms.Find.linear([1, 2, 3, 4, 5, 6],
                                                9),
                         -1)
        self.assertEqual(algorithms.Find.linear([6, 2, 1, 3, 4, 8],
                                                13),
                         -1)
        self.assertEqual(algorithms.Find.linear(['a', 'b', 'c', 'd', 'e', 'f'],
                                                'e'),
                         4)
        self.assertEqual(algorithms.Find.linear(['b', 'c', 'a', 'f', 'd', 'e'],
                                                'c'),
                         1)
        self.assertEqual(algorithms.Find.linear(['a', 'b', 'c', 'd', 'e', 'f'],
                                                'g'),
                         -1)
        self.assertEqual(algorithms.Find.linear(['b', 'c', 'a', 'f', 'd', 'e'],
                                                'm'),
                         -1)
        self.assertEqual(algorithms.Find.linear([[], (3,), [6, 4], 82, 'gg'],
                                                [6, 4]),
                         2)
        self.assertEqual(algorithms.Find.linear([[], (3,), [6, 4], 82, 'gg'],
                                                ()),
                         -1)

    def test_raises(self):
        self.assertRaises(TypeError,
                          algorithms.Find.linear)
        self.assertRaises(TypeError,
                          algorithms.Find.linear,
                          100)
        self.assertRaises(ValueError,
                          algorithms.Sort.quick,
                          {'key': 'value'})


class TestBinaryFind(TestCase):
    def test_equal(self):
        self.assertEqual(algorithms.Find.binary([1, 2, 3, 4, 5, 6],
                                                3),
                         2)
        self.assertEqual(algorithms.Find.binary([1, 2, 3, 4, 5, 6],
                                                9),
                         -1)
        self.assertEqual(algorithms.Find.binary(['a', 'b', 'c', 'd', 'e', 'f'],
                                                'e'),
                         4)
        self.assertEqual(algorithms.Find.binary(['a', 'b', 'c', 'd', 'e', 'f'],
                                                'g'),
                         -1)

    def test_raises(self):
        self.assertRaises(TypeError,
                          algorithms.Find.binary)
        self.assertRaises(TypeError,
                          algorithms.Find.binary,
                          100)
        self.assertRaises(ValueError,
                          algorithms.Sort.quick,
                          {'key': 'value'})
