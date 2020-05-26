import pytest
import random

import selection_sort


def test_quick_sort():
    lst = [random.randint(1, 100) for _ in range(0, 30)]
    assert selection_sort.selection_sort(lst) == sorted(lst)
