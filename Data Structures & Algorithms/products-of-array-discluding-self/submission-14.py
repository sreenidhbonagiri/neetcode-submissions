class Solution:
    # 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prefix = 1
        left_list = []

        for num in nums:
            left_list.append(left_prefix)
            left_prefix *= num

        right_postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            left_list[i] *= right_postfix
            right_postfix *= nums[i]


        return left_list



    