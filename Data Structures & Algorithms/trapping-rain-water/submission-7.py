class Solution:
    # Okay so for this problem we can use two pointers. So left it starting and right will start at the end of the list. Then we can also set a water variable to hold the total amount of water. Then we can also have a left_max and right_max variable which hold the highest walls from either the left side or the right side.
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
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


        