import find_max


def test_find_max_negative_numbers():
    assert find_max.find_max([-20, -30, -20, -200]) == -20


def test_find_max_signed_numbers():
    assert find_max.find_max([-20, -30, -20, -200, 10, 200]) == 200
