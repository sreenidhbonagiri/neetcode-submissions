class Solution:
    # Search through the list for the lowest element, and then set that index to left and set right to the max
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        
        return nums[right]
        