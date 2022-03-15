"""
Author: @sowjanyagarapati
Question: You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith customer has in the jth bank. 
Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
"""

#solution
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
       return max(sum(accounts[i]) for i in range(len(accounts)))
    
