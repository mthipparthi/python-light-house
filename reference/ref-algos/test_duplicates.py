import duplicates


def test_duplicates_positive():
    assert duplicates.duplicates_v1([1, 1, 2, 3,]) == True
    assert duplicates.duplicates_v2([1, 1, 2, 3,]) == True


def test_duplicates_negative():
    assert duplicates.duplicates_v1([1, 4, 2, 3,]) == False
    assert duplicates.duplicates_v2([1, 4, 2, 3,]) == False


def test_duplicates_negative_2():
    assert duplicates.duplicates_v1([1, 4, 2, 3, 1]) == True
    assert duplicates.duplicates_v2([1, 4, 2, 3, 1]) == True
