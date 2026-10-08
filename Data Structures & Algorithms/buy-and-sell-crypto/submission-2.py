class Solution:
    # We can use two pointers again here. So one pointer will be stay at a certain day, the other will go through all of the other options until it hits the first pointer and each time will subtract each price so price[right] - price[left] and if that becomes a negative value we can skip over it. And keep a running total and have print out the maximum profit.
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        total_profit = 0

        while right < len(prices):
            profit = prices[right] - prices[left]

            if profit > 0:
                total_profit = max(profit, total_profit)
                right += 1
            else:
                left = right
                right += 1

        return total_profit
            


       




        