"""
Author: @sowjanyagarapati
Question:There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.
"""

#solution
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for oper in operations:
            if '--' in oper:
                X-=1
            else:
                X+=1
        return X
