'''Approach: 
two pointers:

i = 1
j = 1
we start the loop from 1 and compare it with its previous index element
if n[i] ! = n[i-1]
then we copy the index value with the i value, that way the unique elements get pushed to forward to j postion, 
and then we increment j by 1, i gets automatically incremented in the loop, so at the end we return the j value for unique count.

Time complexity: O(n) in the worst case, where n is the length of the input list. 
Each pointer moves at most n times combined, so overall linear.

Space complexity: O(1) extra space, since only a few variables are used regardless of input size.
'''


def removeDuplicates(self, nums: List[int]) -> int:
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1
    return j