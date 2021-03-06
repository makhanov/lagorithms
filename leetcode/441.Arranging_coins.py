'''
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.
'''
#binary Search
def arrangeCoins(n):
    staircases = 0
    total = 0
    if (n==1):
        return 1

    for i in range(1,n):
        total += i
        if (total>n):
            break
        staircases += 1

    return staircases
