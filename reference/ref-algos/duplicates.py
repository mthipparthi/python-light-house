def duplicates_v1(numbers):
    for i, _ in enumerate(numbers):
        for j, _ in enumerate(numbers):
            if i != j and numbers[i] == numbers[j]:
                return True
    return False


def duplicates_v2(numbers):

    array_len = len(numbers)
    for i in range(array_len):
        for j in range(i + 1, array_len):
            if numbers[i] == numbers[j]:
                return True
    return False


if __name__ == "__main__":
    duplicates_v2([1, 2, 3, 4])
