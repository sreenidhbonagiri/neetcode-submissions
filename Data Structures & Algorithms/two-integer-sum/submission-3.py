class Solution:
    # Plan:
    # We can create map with the keys as the number and values as the index
    # Then we can loop through the list and check to see if the current num's complimnet is in the map, and if not then we just add the current number into our map with its index as the value
    # Then if the complament number is in the map, then we can just return the indexes
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for index, num in enumerate(nums):
            y = target - num

            if y in hash:
                return [hash[y], index]
            
            hash[num] = index
        
                

        