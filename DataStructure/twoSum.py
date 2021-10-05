"""Author @Sowjanya"""
"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target."""



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if(i==len(nums)-1):
                break
            elif(sum([nums[i],nums[i+1]])==target):
                return [i,i+1]
        
