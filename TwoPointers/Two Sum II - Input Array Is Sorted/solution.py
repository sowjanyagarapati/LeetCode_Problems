## brute force O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pairMap = {}
        for i,v in enumerate(numbers):
            pair = target - v
            if pair not in pairMap:
                pairMap[v] = i+1
            else:
                return [pairMap.get(pair), i+1]


## optimal
        