import fizzbuzz


def test_fizbuzz():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
    assert fizzbuzz.main(numbers) == [
        1,
        2,
        "Fizz",
        4,
        "Buzz",
        "Fizz",
        7,
        8,
        "Fizz",
        "Buzz",
        "FizzBuzz",
    ]
