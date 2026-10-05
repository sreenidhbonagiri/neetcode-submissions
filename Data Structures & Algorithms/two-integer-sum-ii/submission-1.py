class Solution:
    # Guess we can have two pointers one from the beginning and one at the end. We sum the numbers up initially and check whether that equals target or not. If it does great return those indexes + 1, if the sum is greater than the target then we can decrement our right pointer. If the sum is lower than the target we can increment our left pointer. Then loop this shit until the sum adds to the target.
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1   
        total = 0

        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1

        return [left + 1, right + 1]

            
