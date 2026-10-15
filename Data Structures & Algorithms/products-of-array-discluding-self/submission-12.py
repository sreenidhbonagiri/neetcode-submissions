class Solution:
    # 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        result = []

        for num in nums:
            result.append(left)
            left *= num

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right
            right *= nums[i]


        return result




        