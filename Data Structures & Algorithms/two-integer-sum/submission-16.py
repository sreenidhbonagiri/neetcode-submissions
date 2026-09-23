class Solution:
    # We can make a index map that contains each number as the key and its value is just its index.
    # Then we can loop through the nums list until we find the complement number to the target.
    # Once we find it, then we can just return the index of the current number plus the complements index by returning the value. 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for index, number in enumerate(nums):
            complement = target - number

            if complement in map:
                return sorted([index, map[complement]])

            map[number] = index
    
        
                
        

     

        
                

        