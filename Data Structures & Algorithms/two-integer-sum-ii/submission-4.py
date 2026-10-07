class Solution:
    # We can just have two pointers left and right. And as we loop the list while left < right we can check if numbers[left] + nums[right] equals the target and if it does then we can return its indexes + 1. If the sum of the two is less than the target then we can move our left pointer inward. If the sum of the two is more than the targe tthen we can move our right pointer inward.
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
  
        left = 0
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -=1 


      