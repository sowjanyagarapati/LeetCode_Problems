''' Author @sowjanyagarpati
Question: Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.'''


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    c+=1
        return c
                  
