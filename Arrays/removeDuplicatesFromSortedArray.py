'''Author: @sowjanyagarapati'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums2 = sorted(list(set(nums)))
        after_len = len(nums2)
        for i in range(after_len):
            nums[i]=nums2[i]
        return after_len
