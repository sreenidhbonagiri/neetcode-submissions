class Solution:
    # Want to have a prefix variable equalling 1. And then basically loop through nums and append to the left list the element which you will set equal to the prefix variable. And then update prefix variable after multiplying it with the element. Then do the same thing again but with a right list and a postfix and loop starting from the end all the way down. Then invert that right list. Then create a new list which will the one we are returning and go through the left list and multiply each element of that list with the inverted right list and set that as the return list.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        prefix = 1

        for num in nums:
            left.append(prefix)
            prefix *= num

        inv_right = []
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            inv_right.append(postfix)
            postfix *= nums[i]

        right = inv_right[::-1]

        result = []

        for i in range(len(left)):
            result.append(left[i] * right[i])

        return result

        


        

            
        