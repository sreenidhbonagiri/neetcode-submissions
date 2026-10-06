class Solution:
    # First we can set two pointers left and right. Also have to set an area variable to 0 to keep track of area values. Then we can loop until left < right and then we can set a width variable equal to right - left. Then we can set height variable to the min of the two. Then we can set the current area variable equal to the height times the width. Then we can set our area variable from earlier equal to the max of the current area and total area values. Then we can check if left height is smaller than the right height then we can move our left inward. If the right height is smaller than the left height then we can also move our right inward. And if both are equal then we just move both inward.
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            curr_area = height * width
            area = max(curr_area, area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1

        return area




       


        
