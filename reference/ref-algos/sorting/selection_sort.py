


def selection_sort(numbers):
    length = len(numbers)
    for i in range(length):
        min_index = i
        for j in range(i+1, length):
            if numbers[j] < numbers[min_index]:
                min_index = j
                
        numbers[i] , numbers[min_index] = numbers[min_index] , numbers[i]
        
        # print(numbers)
        
    return numbers


# 1. Create result list
# 2. Find biggest.smallest item in the list and add to result list
# 3. contine to fins next biggest and add to list
# 4. if you will have sorted list

def find_smallest_index(items):
    small_index = 0
    for index, item in enumerate(items):
        if item < items[small_index]:
            small_index = index 
    return small_index
        

def selection_sort_v2(items):
    for i in range(len(items)):
        small_index = find_smallest_index(items[i:])
        items[i], items[i+small_index] = items[i+small_index], items[i]
    return items
 
                
if __name__ == "__main__":
    print(selection_sort([6,7,4,5,2,3,9]))
    print(selection_sort_v2([6,7,4,5,2,3,9])) 
    
# [6, 7, 4, 5, 2, 3, 9]   
# [2, 7, 4, 5, 6, 3, 9]
# [2, 3, 4, 5, 6, 7, 9]
# [2, 3, 4, 5, 6, 7, 9]
# [2, 3, 4, 5, 6, 7, 9]
# [2, 3, 4, 5, 6, 7, 9]
# [2, 3, 4, 5, 6, 7, 9]
# [2, 3, 4, 5, 6, 7, 9]
# [2, 3, 4, 5, 6, 7, 9]