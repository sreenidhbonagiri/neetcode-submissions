class Solution:
    # Plan:
    # We can have a list called output. Then we can loop through the list, and keep track of the index and number. And 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        output = [0] * n
        l_mult = 1
        for i in range(n):
            output[i] = l_mult
            l_mult = l_mult * nums[i]

        r_mult = 1
        for i in range(n - 1, -1, -1):
            output[i] *= r_mult
            r_mult = r_mult * nums[i]

        return output



            
        