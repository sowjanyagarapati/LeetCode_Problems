'''Approach:
Initialize closest with first element
Iterate through the array and compare the absolute value of the current element 
with the absolute value of the closest element
if the absolute value of the current element is less than the 
absolute value of the closest element, then update the closest element
Time Complexity: O(n) + O(n) = O(2n) = O(n)
Space Complexity: O(1)


'''


def findClosestNumber(self, nums: list[int]) -> int:
    closest = nums[0]
    for num in nums: # O(n)
        if abs(num) < closest:
            closest = num
    if closest < 0 and abs(closest) in nums: # O(n)
        return abs(closest)
    else:
        return closest