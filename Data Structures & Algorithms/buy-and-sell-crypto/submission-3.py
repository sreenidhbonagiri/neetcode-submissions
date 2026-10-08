class Solution:
    # We are trying to buy low and sell high. We can have two pointers one left and one right. We can set both equal to 0 at the start. We can also have a total_profit variable which will hold our total profit. Then we can loop through until right reaches the end of the list. Then we can check if right - left is a positive number, because if it is then we can make our left pointer equal to our right pointer?
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        total_profit = 0

        while right < len(prices):
            if prices[right] - prices[left] < 0:
                left = right
                right += 1
            else:
                curr_profit = prices[right] - prices[left]
                total_profit = max(curr_profit, total_profit)

                right += 1
        

        return total_profit

        