## brute force O(n)

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    pairMap = {}
    for i,v in enumerate(numbers):
        pair = target - v
        if pair not in pairMap:
            pairMap[v] = i+1
        else:
            return [pairMap.get(pair), i+1]


## optimal Two pointers O(n)
'''
Approach: 
The two pointers start and end are initialized to the first and last indices of the array respectively.
if the sum is equal to the target, return the indices.
else if the sum is less than the target, increment the start pointer.
else decrement the end pointer.
'''

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    start = 0
    end = len(numbers) - 1
    while start < end:
        result = numbers[start] + numbers[end]
        if result == target:
            return [start+1, end+1]
        elif result < target:
            start +=1
        else:
            end -=1
    return [-1, -1]

'''
Time complexity: O(n) in the worst case, where n is the length of the input list. Each pointer moves at most n times combined, so overall linear.

Space complexity: O(1) extra space, since only a few variables are used regardless of input size.
'''
        