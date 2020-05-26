



def insertion_sort(numbers):
    for i in range(len(numbers)):
        for j in range(i+1):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                
    return numbers


# [6, 5, 3, 1, 8, 7, 2, 4]
# [5, 6, 3, 1, 8, 7, 2, 4]
# [3, 5, 6, 1, 8, 7, 2, 4]
# [1, 3, 5, 6, 8, 7, 2, 4]
# [1, 3, 5, 6, 8, 7, 2, 4]
# [1, 3, 5, 6, 7, 8, 2, 4]
# [1, 2, 3, 5, 6, 7, 8, 4]
# [1, 2, 3, 4, 5, 6, 7, 8]
# [1, 2, 3, 4, 5, 6, 7, 8]

if __name__ == "__main__":
    print(insertion_sort([6, 5, 3, 1, 8, 7, 2, 4]))