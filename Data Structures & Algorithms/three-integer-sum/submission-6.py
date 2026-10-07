class Solution:
    # First we have to sort our nums list. Then we can go through each elemnet of the list and keep track of nums[i]. Then we can first check for duplicate handling. And then we can use two pointers left and right. Then make a loop while left < right, we can then create a total variable which would equal the sum of nums[i] and nums[left] and nums[right]. Then we can check if the sum is 0, then we can move our pointers inward and append our triplet into our result list. Then after that we can check for duplicate handling to make sure the next pairs arent duplicate. Then check if the sum is < 0 and if is then we can move our left pointer inward. If the sum is > 0, we can move our right pointer inward. And then just return the result list.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            total = 0

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -=1 

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

            







       

                 
        

                

            



        


        