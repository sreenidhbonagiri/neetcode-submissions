class Solution:
    # We can first go through every num in nums, and then first we can subtract the target by that num and we get the other number that we are looking for. Then we loop through again to find the other number, and if we find it then we track its index and return the sorted list of both the indices.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, number in enumerate(nums):
            diff = target - number

            if diff in seen:
                return sorted([seen[diff], index])
            
            seen[number] = index
        
        return []
     

        
                

        