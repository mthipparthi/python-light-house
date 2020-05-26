# Quicksort is a sorting algorithm that picks an element ("the pivot") and reorders the array forming two partitions such that all elements less than the pivot come before it and all elements greater come after. The algorithm is then applied recursively to the partitions until the list is sorted.


def quick_sort(numbers):

    if len(numbers) <= 1:
        return numbers

    pivot = numbers[len(numbers) // 2]

    left = [i for i in numbers if i < pivot]
    mid = [i for i in numbers if i == pivot]
    right = [i for i in numbers if i > pivot]

    return quick_sort(left) + mid + quick_sort(right)


if __name__ == "__main__":
    print(quick_sort([6, 5, 3, 1, 8, 7, 2, 4]))
