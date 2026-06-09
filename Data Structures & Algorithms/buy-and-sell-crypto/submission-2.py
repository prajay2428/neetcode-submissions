class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit=0
        curr_price=prices[0]
        profit=0

        for i in range(1,n):
            if prices[i] < curr_price:
                curr_price=prices[i]
                continue
            profit = prices[i] - curr_price
            max_profit = max(profit,max_profit)

        return max_profit
      
        