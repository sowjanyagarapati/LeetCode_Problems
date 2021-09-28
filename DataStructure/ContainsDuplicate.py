'''Author @Sowjanya '''
''' This Program returns true if a list contains duplicates else returns false'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==len(set(nums)):
            return False
        else:
            return True
        
