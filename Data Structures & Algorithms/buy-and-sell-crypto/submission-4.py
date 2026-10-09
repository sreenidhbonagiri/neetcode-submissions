class Solution:
    # We are trying to buy the lowest point and find the highest point to sell. So we can have to pointers left and right. Both will start at 0, And we can check while right goes to the end of the list, we can check each time if right - left = positive or negative. See if its a negative that means the right is a lower price so we can change our left to our right pointer to buy. And then we can keep checking and if the right - left is a positive number then thats our profit we can calculate with. Then with a total profit variable we can keep track of the biggest profits and return that one.
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
                total_profit = max(curr_profit, total_profit)
                right += 1

        return total_profit


        