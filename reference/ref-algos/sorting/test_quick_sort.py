import pytest
import random

import quick_sort


def test_quick_sort():
    lst = [random.randint(1, 100) for _ in range(0, 30)]
    assert quick_sort.quick_sort(lst) == sorted(lst)
