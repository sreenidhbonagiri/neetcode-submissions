class Solution:
    # So we can use two pointers left and right. So left will begin at the start and right will be at the end. Then we can just calculate the width by subtracting the right and left. Then we can calculate the height. And calculate the current area
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        total_area = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            curr_area = height * width
            total_area = max(total_area, curr_area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1

        return total_area
        
        


        

            
            
        


       


        
