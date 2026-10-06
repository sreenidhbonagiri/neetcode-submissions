class Solution:
    # Could use two pointers to find two heights. Can have a max variable that keeps track of the biggest area. And then we keep moving the pointer with the smaller height as thats the height we will you use for the calculation. 
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            curr_area = width * height
            area = max(area, curr_area)

            if heights[left] > heights[right]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
            elif heights[left] == heights[right]:
                left += 1
                right -= 1

        return area
