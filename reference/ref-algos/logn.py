def logn(num):
    i = 1
    steps = 0
    while i < num:
        i = i * 2
        steps += 1

    return steps


# L is a sorted list containing n signed integers (n being big enough), for example [-5,-2,-1,0,1,2,4]
# (here, n has a value of 7). If L is known to contain the integer 0, how can you find the index of 0 ?


def find_index(numbers, search_num):
    low = 0
    high = len(numbers) - 1
    while low < high:
        mid = (low + high) // 2
        if numbers[mid] == search_num:
            return mid
        elif numbers[mid] < search_num:
            low = mid
        elif numbers[mid] > search_num:
            high = mid


if __name__ == "__main__":
    print(logn(20))
