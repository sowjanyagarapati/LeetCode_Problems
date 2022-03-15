"""
Author: @sowjanyagarapati
Question: Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""

#solution
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newlist = []
        list1 = nums[0:n]
        list2 = nums[n:len(nums)]
        for i in range(len(list1)):
            newlist.append(list1[i])
            newlist.append(list2[i])
        return newlist
