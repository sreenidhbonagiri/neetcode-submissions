class Solution:
    # Okay so first we loop through the nums list and have our initial number nums[i]. Now using two pointers we have to find two numbers that to nums[i] and equalling 0. Also have to handle duplicate checks by making sure that if nums[i] == nums[i + 1] then we just continue and so on. 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            initial = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = initial + nums[left] + nums[right]

                if total == 0:
                    result.append([initial, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result








       

                 
        

                

            



        


        