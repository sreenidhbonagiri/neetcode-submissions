class Solution:
    # First create a total area variable and set it to 0 for now. We can use two pointers for this problem. So we can have our left and right pointers, and keep looping until left < right. Then for each iteration we can check for the width by doing right - left. Then we can get height by doing min(heights[left], heights[right]) Then calculating the area by multiplying the both which gives us the current area. Then we can update our total area variable equal it to the max of the total area and the current area. Then we can continue looping until the end. And then just return the total area.
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            curr_area = width * height
            max_area = max(max_area, curr_area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1

        return max_area


        

            
            
        


       


        
