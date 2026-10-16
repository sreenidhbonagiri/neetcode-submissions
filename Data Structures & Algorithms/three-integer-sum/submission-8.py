class Solution:
    # We can use two pointers left and right. And can loop through the list, keeping track of nums[i] as well. And then we are trying to find two other variables that sum with nums[i] that equal 0. We also ned to make sure we are looking out for duplicates in the beginning and for everytime we move our pointers.
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
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -=1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

                
        return result


        


       

                 
        

                

            



        


        