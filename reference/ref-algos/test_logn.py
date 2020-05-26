import logn
import math


def test_logn():

    assert logn.logn(20) == int(math.log2(20)) + 1
    assert logn.logn(200) == int(math.log2(200)) + 1
    assert logn.logn(2000) == int(math.log2(2000)) + 1
    assert logn.find_index([-5, -2, -1, 0, 1, 2, 4], 0) == 3
    assert logn.find_index([-5, -2, -1, 0, 0, 1, 2, 4], 0) == 3
