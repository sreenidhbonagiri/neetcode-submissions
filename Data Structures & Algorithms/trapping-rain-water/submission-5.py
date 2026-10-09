class Solution:
    # For this we can use two pointers, left and right and we can set left to 0 and right to the length of the list - 1. Then we can also create two more variables left max and right max which we can set equal to the heigh[left] and height[right] just to start off with. Then in our loop we can check for which wall is bigger, so if the right wall is bigger then we only have to take care of our left wall. Then we can basically move our left pointer to see if we can get a bigger left wall. We also want to update our left max with the max of itself and the new left pointer. And then we can add water by calculating left wall - height of the left. And do the same with our right wall. And then return the total running count of water.
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]

        water = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(height[left], left_max)
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(height[right], right_max)
                water += right_max - height[right]

        return water


       