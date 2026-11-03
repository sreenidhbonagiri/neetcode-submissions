class Solution:
    # Okay so for this problem, we can have 
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)

        for index, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                popped_index = stack.pop()
                popped_height = heights[popped_index]

                if stack:
                    width = index - stack[-1] - 1
                else:
                    width = index
                
                area = width * popped_height
                max_area = max(max_area, area)
            
            stack.append(index)

        return max_area


        