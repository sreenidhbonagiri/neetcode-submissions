class Solution:
    # We can just go through the list and have two pointers left and right. So for each of the two pointers we just calculate their width by subtracting their indexes. Then we can calculate their height with just comparing the two pointers actual numbers and using the min function. Then we can set the current area variable equal to the multiplication of the height and the width. We can also have a total area variable at the top and each time a current area is done computing we compare it with the total area and set the bigger one to total area. And loop that until its done and just return the total area.
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
                left +=1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1

        return total_area


            

            
            
        


       


        
