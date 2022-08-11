### 121. Best Time to Buy and Sell Stock 22/08/11###

###My Solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0

        for price in prices:
            if price < min:
                min = price

            if price > min and (price - min) > profit:
                profit = price - min

        return profit


### Similar but compact solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price

            max_profit = max(max_profit, profit)

        return max_profit