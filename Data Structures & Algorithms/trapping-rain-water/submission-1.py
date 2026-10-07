class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        curr_max = 0

        for i in range(len(height)):
            left_max.append(curr_max)
            curr_max = max(curr_max, height[i])

        inv_right_max = []
        new_max = 0
        for i in range(len(height) - 1, -1, -1):
            inv_right_max.append(new_max)
            new_max = max(new_max, height[i])

        right_max = inv_right_max[::-1]

        total = 0 
        for i in range(len(height)):
            water = min(left_max[i], right_max[i]) - height[i]

            if water > 0:
                total += water


        return total

        

