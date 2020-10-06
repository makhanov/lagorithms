# ins = input().strip()

# is_pm = ins[-2:].lower() == 'pm'
# time_list = list(map(int, ins[:-2].split(':')))

# if is_pm and time_list[0] < 12:
#     time_list[0] += 12

# if not is_pm and time_list[0] == 12:
#     time_list[0] = 0

# print(':'.join(map(lambda x: str(x).rjust(2, '0'), time_list)))


"""
Sorting algorithms in python3 
"""

# Selection sort
import random


random_list = [random.randrange(1,100,1) for i in range(10)]

def selectionSort(arr):
    
    arr_size = len(arr)
    
    for i in range(arr_size-1):
        for j in range(i+1, arr_size):
            if arr[i] >= arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    
    return arr

print(f"A random list of numbers: {random_list}")
print(f"Sorted (ascending order) list: {selectionSort(random_list)}")