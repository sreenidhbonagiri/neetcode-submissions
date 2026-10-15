class Solution:
    # We can basically create a left prefix variable and set it equal to 1 to start with. And for each number in nums, we can multiply it with prefix, and then we can update prefix to multiply it with the first element in the list and set that element to the return list. Then we can keep looping that till it goes to the end of the list. And we can do the same for the suffix but for tha we have to start from the end of nums and go backward. And do the same thing. Then invert it. And then just return the return list.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        result = []

        for num in nums:
            result.append(left)
            left *= num

        right = 1
        
        for num in range(len(nums) - 1, -1, -1):
            result[num] *= right
            right *= nums[num]

        return result
      

        