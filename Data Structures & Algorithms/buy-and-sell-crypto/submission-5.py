class Solution:
    # We want to buy low and sell high and return the maximum amount of profit that we can get. So we can have two pointers left and right as well as a running sum total variable. Then we can loop until right goes to the end of the list, and we can check if right is bigger than left. If right is lower, then we can set our left pointer equal to our right pointer and increment our right. If the right is bigger then we can calculate right - left and set that equal to a count variable. And compare it to our running sum and keep the max. And increment our right only. Then we can just return our sum. 
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        total_profit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                curr_profit = prices[right] - prices[left]
                total_profit = max(total_profit, curr_profit)
                right += 1

        return total_profit



        

        