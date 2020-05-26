# Merge Sort is a divide-and-conquer algorithm. It divides the input list of length n in half successively until there are n lists of size 1. Then, pairs of lists are merged together with the smaller first element among the pair of lists being added in each step. Through successive merging and through comparison of first elements, the sorted list is built.


#  [10,20] [15,25]
def merge_lists(list1, list2):
    print("merge_lists:b")
    print(list1)
    print(list2)
    print("merge_lists:e")
    rv = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            rv.append(list1[i])
            i += 1
        else:
            rv.append(list2[j])
            j += 1
    rv += list1[i:] + list2[j:]

    return rv


def merge_sort(numbers):
    length = len(numbers)
    if length == 1:
        return numbers

    print(numbers)

    mid = length // 2

    return merge_lists(merge_sort(numbers[:mid]), merge_sort(numbers[mid:]))


if __name__ == "__main__":
    print(merge_sort([6, 5, 3, 1, 8, 7, 2, 4]))
