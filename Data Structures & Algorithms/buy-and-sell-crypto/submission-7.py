class Solution:
    # We are calculating max profit so we want to buy lowest and sell highest. We can use two pointers to search through the list, left and right. And we can set both at 0 to start, and then as right moves forward, we can check if right - left is > 0, if it is then we keep moving if not, then we set our left to right since right is smaller. And each time if it is > 0, we calculate the profit, and then store it in a current value. And then set total equal to the max of the curent and total and repeat untl right hits the end of the list.
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        total_profit = 0

        for right in range(len(prices)):
            curr_profit = prices[right] - prices[left]

            if curr_profit > 0:
                total_profit = max(total_profit, curr_profit)
            else:
                left = right
            
            
        return total_profit

        




               


    