import pytest
import random

import insertion_sort


def test_merge_sort():
    lst = [random.randint(1, 100) for _ in range(0, 30)]
    assert insertion_sort.insertion_sort(lst) == sorted(lst)
