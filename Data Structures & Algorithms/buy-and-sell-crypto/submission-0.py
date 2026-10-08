class Solution:
    # We can use two pointers again here. So one pointer will be stay at a certain day, the other will go through all of the other options until it hits the first pointer and each time will subtract each price so price[right] - price[left] and if that becomes a negative value we can skip over it. And keep a running total and have print out the maximum profit.
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for i in range(len(prices)):
            j = i + 1

            while j < len(prices):

                if prices[j] - prices[i] < 0:
                    j += 1
                    continue

                profit = prices[j] - prices[i]

                total_profit = max(profit, total_profit)

                j += 1


        return total_profit
 


        