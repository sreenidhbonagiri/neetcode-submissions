class Solution:
    # We can use two pointers one to start and one coming from the end. We also need a total water variable. We need to check if our left wall is bigger or right wall is bigger. If our left wall is bigger, then
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1 
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water



       
        