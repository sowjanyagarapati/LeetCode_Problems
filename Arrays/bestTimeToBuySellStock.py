'''Approach: 
Array traversal:
initialize min_price = first element
initialize max_profit = 0
for i = 1 to n-1:
    max_profit = max(max_profit, current_price - min_price)
    min_price = min(min_price, current_price)
return max_profit

Time Complexity: O(n)
Space Complexity: O(1)


'''


def maxProfit(self, prices: list[int]) -> int:
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        max_profit = max(max_profit, price-min_price)
        min_price = min(price, min_price)
    return max_profit