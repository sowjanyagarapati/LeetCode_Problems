''' Author @sowjanyagarapati
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.'''


class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        bool_arr = []
        for candy in range(len(candies)):
            candies[candy]+=extraCandies
            if max(candies)==candies[candy]:
                bool_arr.append(1)
            else:
                bool_arr.append(0)
            candies[candy]-=extraCandies
        return bool_arr
