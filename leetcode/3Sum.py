'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.
'''
def threeSum(nums):
    triplets = []
    
    #base case
    if len(nums)<=2:
        return triplets
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            b = nums[i]+nums[j]
            if (b==0):
                if 0 in nums:
                    pair = [nums[i], nums[j], 0]
                    if pair not in triplets:
                        triplets.append(pair)
            c = -(b)
            if c in nums:
                pair = [nums[i], nums[j], c]
                if pair not in triplets:
                    triplets.append(pair)
    return triplets