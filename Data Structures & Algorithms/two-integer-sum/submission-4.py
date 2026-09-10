class Solution:
    # Basically you want to just go through the list of nums, and for each number store their index and the value and calculate it's compliment. Then try to find this compliment number in this nums, and store its index as well as the original number's index. Then just return both the indexes in a list and sort the list so that it returns in least to greatest

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): 
            complament = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == complament:
                    return [i,j]


        
        
                

        