class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        heights.append(0)

        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                popped_index = stack.pop()
                popped_height = heights[popped_index]
                
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = width * popped_height
                max_area = max(area, max_area)
            
            stack.append(i)

        return max_area
        