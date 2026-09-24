class Solution:
    # Thinking that maybe we can ignore the current index number, and multiply all of the other numbers in the list and store it in a value. Then insert that value at the same index in a new list.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

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




            
        