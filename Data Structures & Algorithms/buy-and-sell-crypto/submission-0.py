class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_p = 0

        for i in range (n-1):
            sell_price = prices[0]
            del prices[0]
            buy_price = max(prices)
            profit = buy_price-sell_price

            if profit > max_p:
                max_p = profit
        
        return max(max_p,0)