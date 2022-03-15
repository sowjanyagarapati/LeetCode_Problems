"""
Author: @sowjanyagarapati
Question:Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

#solution
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))]
