class Solution:
    # First find the left wall max values,
    def trap(self, height: List[int]) -> int:
        left = []
        left_max = 0

        for i in range(len(height)):
            left.append(left_max)
            left_max = max(left_max, height[i])

        right = []
        right_max = 0

        for i in range(len(height) - 1, -1, -1):
            right.append(right_max)
            right_max = max(right_max, height[i])

        right = right[::-1]

        total = 0
        for i in range(len(height)):
            water = min(left[i], right[i]) - height[i]

            if water > 0:
                total += water

        return total
