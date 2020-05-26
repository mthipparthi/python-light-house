# [1,2,3,4]


# def binary_search(numbers, num):
#     low = 0
#     high = len(numbers) - 1
#     #  4

#     while low <= high:
#         mid = low + (high - low) // 2
#         if numbers[mid] == num:
#             return True

#         if numbers[mid] < num:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return False


def binary_search(numbers, num):
    low = 0
    high = len(numbers) - 1
    #  4

    while low <= high:
        mid = (low + high) // 2
        if num == numbers[mid]:
            return mid
        elif num > numbers[mid]:
            low = mid + 1
        elif num < numbers[mid]:
            high = mid - 1
    breakpoint()

    return False


def binary_search_v2(items, item):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2
        if item == items[mid]:
            return mid
        elif item < items[mid]:
            high = mid - 1
        elif item > items[mid]:
            low = mid + 1


if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4], 8))
    # print(binary_search_v2([1, 2, 3, 4, 5, 6, 7],))
