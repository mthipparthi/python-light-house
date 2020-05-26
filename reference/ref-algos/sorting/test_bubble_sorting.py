import bubble_sorting

import pytest


@pytest.mark.parametrize("input", [([6, 5, 3, 1, 8, 7, 2, 4])])
def test_bubble_v1(input):
    assert bubble_sorting.bubble_sort_v1(input) == sorted(input)


@pytest.mark.parametrize("input", [([6, 5, 3, 1, 8, 7, 2, 4])])
def test_bubble_v2(input):
    assert bubble_sorting.bubble_sort_v2(input) == sorted(input)
