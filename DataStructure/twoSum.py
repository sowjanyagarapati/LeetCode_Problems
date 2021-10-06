"""Author @Sowjanya"""
"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target."""



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i,n in enumerate(nums):
            if (target-n) in hashMap:
                return [i,hashMap[target-n]]
            else:
                hashMap[n]=i
        
