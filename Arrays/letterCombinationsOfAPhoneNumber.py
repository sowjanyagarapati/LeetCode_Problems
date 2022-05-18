''' Author: @sowjanyagarapati

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.'''


import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {
            '2' : "abc",
            '3' : "def",
            '4' : "ghi",
            '5' : "jkl",
            '6' : "mno",
            '7' : "pqrs",
            '8' : "tuv",
            '9' : "wxyz"
        }
        combinations = []
        digits_map = {}
        if len(digits)==0:
            return combinations
        else:
            for i in digits:
                ele = list(mappings[i])
                combinations.append(ele)
        return ["".join(i) for i in itertools.product(*combinations)]
