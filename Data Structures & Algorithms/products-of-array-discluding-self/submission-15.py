class Solution:
    # We can use prefixes and postfixes here. So we can create a left prefix 1, and create our result list. Now we can go through each element in nums and for each we will first append our prefix, then we will multiply our prefix with that element, and keep looping that until we get to the end of our list. So we are trying to get a list of all the products from the left side of the array first. Then we can move on to our right side by creating a postfix of 1, and then looping through the nums list starting from the end. Then we will modify our result list by multipling each element with the value of our right postfix which starts off at 1. Then we can modify our right postfix by multipling it with each element. And so we have multiplied our left products with our right products to create a list of all the products of the array except for itself.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prefix = 1
        result = []

        for num in nums:
            result.append(left_prefix)
            left_prefix *= num

        right_postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right_postfix
            right_postfix *= nums[i]

        return result
        

        

     