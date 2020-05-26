import pytest
import random
import merge_sorting

# @pytest.mark.parametrize("input", [([6, 5, 3, 1, 8, 7, 2, 4])])
# def test_bubble_v1(input):
#     assert merge_sorting.merge_sort(input) == sorted(input)


@pytest.mark.parametrize(
    "list1, list2, expected", [([10, 20], [15, 25], [10, 15, 20, 25])]
)
def test_merge_list(list1, list2, expected):
    assert merge_sorting.merge_lists(list1, list2) == expected


def test_merge_sort():
    lst = [random.randint(1, 100) for _ in range(0, 30)]
    print(lst)
    assert merge_sorting.merge_sort(lst) == sorted(lst)
