'''Author: @sowjanyagarapati'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = int(''.join(str(val) for i,val in enumerate(digits)))+1
        return [int(a) for a in str(last)]
