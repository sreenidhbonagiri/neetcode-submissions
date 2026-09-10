class Solution:
    # We can first go through every num in nums, and then first we can subtract the target by that num and we get the other number that we are looking for. Then we loop through again to find the other number, and if we find it then we track its index and return the sorted list of both the indices.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == diff:
                    return sorted([i,j])
        return []
     

        
                

        