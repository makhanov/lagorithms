# Insertion sort

import random


rand_list = random.sample(range(1,50,1),10)
def insertionSort(arr):
    for i in range(1,len(arr)):
        maxVal = arr[i]
        j = i - 1 
        while j >= 0 and maxVal < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = maxVal
    return arr
print (rand_list)
print (insertionSort(rand_list))
