'''Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.'''
#O(n)
def twoSum(nums, target):
    #build a hash table
    table = {}
    for i in range(len(nums)):
        table[i] = nums[i]
        
    for i in range(len(nums)):
        second_num = target - nums[i]
        dupl = {k:v for k,v in table.items() if k > i}
        if second_num in dupl.values():
            keys = list(dupl.keys())
            vals = list(dupl.values())
            second_index = keys[vals.index(second_num)]
            return [i, second_index]

#second brute-force method
#O(n^2)
def twoSumv2(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            second_num = target - nums[i]
            if second_num == nums[j]:
                return [i, j]
