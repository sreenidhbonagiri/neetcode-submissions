class Solution:
    # First we can sort the nums list. Then we can create our left and right pointers. Then we can keep loop through every element in nums. And then also check if i > 0 and nums[i] == nums[i -1] then we can just skip it. Then we can create another loop that goes until left < right. And then in that loop we can create a total variable which is just nums[i] + nums[left] + nums[right]. And we can check if total = 0, and if it does then we can append those three values in a list to the result list. Then we can increment our left and right pointers. Now if the total is less than 0, then that would mean we need to increment our left pointer. Now if the total is greater than 0, then we have to decrement our right pointer. And we also have to check while left<right and nums[left] == nums[left - 1] and nums[right] = nums[right + 1] for duplicate handling. And then just return result.
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
                        right -= 1
                
                elif total < 0:
                    left += 1
                else:
                    right -= 1


        return result

       








       

                 
        

                

            



        


        