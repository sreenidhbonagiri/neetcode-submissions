class Solution:
    # For this problem we can use binary search. So first we can use two pointers left and right. And we can also have a mid variable that will hold the index to the middle number of the list which we can set equal to mid = left + right // 2. Then we can loop through until left <= right. At each iteration we can check if the target value is equal to our mid value, if so then we can just return mid. If not we can check if the target value is greater than the number at mid, if so, then we can set our left index to mid + 1. If the target value is less than the number at mid, then we can set our right index to mid - 1.   
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            elif target > nums[mid]:
                left = mid + 1

            elif target < nums[mid]:
                right = mid - 1

        return -1

      