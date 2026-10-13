class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy, sell = 0, 1

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                current_profit = prices[sell] - prices[buy]
                max_profit = max(current_profit, max_profit)
            else:
                buy = sell 
            sell += 1

        return max_profit