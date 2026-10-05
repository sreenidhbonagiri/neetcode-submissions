class Solution:
    # If you choose a number nums[i] then the other two numbers have to add up to -nums[i]. First sort the array and then loop through the list and treat the first element as the nums[i], and then use two pointers to find two elements that add up to -nums[i]. 
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
                    left +=1 
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1

        return result
        

                

            



        


        