import binary_serach


def test_binary_serach():
    assert binary_serach.binary_search([1, 3, 3, 4, 5, 6, 7, 8, 34], 8)
    assert not binary_serach.binary_search([1, 3, 3, 4, 5, 6, 7, 8, 34], 80)
    assert binary_serach.binary_search([1, 3, 3, 4, 5, 6, 7, 8, 34], 34)

    assert binary_serach.binary_search_v2([1, 3, 3, 4, 5, 6, 7, 8, 34], 8)
    assert not binary_serach.binary_search_v2([1, 3, 3, 4, 5, 6, 7, 8, 34], 80)
    assert binary_serach.binary_search_v2([1, 3, 3, 4, 5, 6, 7, 8, 34], 34)
