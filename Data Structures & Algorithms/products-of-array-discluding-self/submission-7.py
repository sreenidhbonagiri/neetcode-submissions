class Solution:
    # I would create a prefix variable and set it to 1. Then I would make a new left list. Then I would loop through the nums list, and for each element I would multiply it with the prefix. And then update the prefix *= current element. Then I would do the same with the right list. So I would make an invert right list. And make a postfix variable and set it to 1 as well. But this time we are going to be looping from the end and decrementing. Then I would just invert that right list by using [::-1]. Then I would loop through each element in the left list, and for each element I would multiply it with the corresponding element in the right list and append that value to the result list until the full left list is done.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        left = []
        for i in range(len(nums)):
            left.append(prefix)
            prefix *= nums[i]

        postfix = 1
        inv_right = []
        for i in range(len(nums) - 1, -1, -1):
            inv_right.append(postfix)
            postfix *= nums[i]

        right = inv_right[::-1]

        result = []
        for i in range(len(left)):
            result.append(left[i] * right[i])

        return result



            
        