import nose.tools as nt
from random import choice

def quicksort_val(array):
    if len(array) <= 1:
        return array
    lower, upper, center = [], [], []
    part = choice(array)
    for i in array:
        if i < part:
            lower.append(i)
        elif i > part:
            upper.append(i)
        else:
            center.append(i)
    return (quicksort_val(lower) +
            center +
            quicksort_val(upper))


def test_sanity():
    nt.assert_equal(quicksort_val([3, 2, 1]),
                    [1, 2, 3])
    nt.assert_equal(quicksort_val([100, 1000, 10]),
                    [10, 100, 1000])
    nt.assert_equal(quicksort_val(['a', 'c', 'b']),
                    ['a', 'b', 'c'])


def test_extended():
    # Test single element
    nt.assert_equal(quicksort_val([1]),
                    [1])
    # Test empty list
    nt.assert_equal(quicksort_val([]),
                    [])
    # Test duplicates
    nt.assert_equal(quicksort_val([1, 2, 2, 1]),
                    [1, 1, 2, 2])
    # Test mixing types
    nt.assert_equal(quicksort_val(['abc', 1, 1.0]),
                    [1, 1.0, 'abc'])
