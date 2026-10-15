class Solution:
    # 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        left_list = []

        for num in nums:
            left_list.append(left)
            left *= num

        right = 1
        right_list = []

        for i in range(len(nums) - 1, -1, -1):
            right_list.append(right)
            right *= nums[i]

        right_list = right_list[::-1]

        result = []
        for i in range(len(left_list)):
            result.append(left_list[i] * right_list[i])

        return result




        