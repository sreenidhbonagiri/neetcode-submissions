class Solution:
    # So we can loop through the nums list and keep track of nums[i]. We also can check for duplicates to make sure nums[i] is different. Then we can also have a left and right pointer which will point to our other 2 numbers. 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            
            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -=1

                    while left < right and nums[left] == nums[left - 1]:
                        left +=1 
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -=1
                
        return result




            
            


      