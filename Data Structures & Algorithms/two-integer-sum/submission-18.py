class Solution:
    # We can loop through the list, and for each number we can calculate its complement. And while we are going through the list we can also have a map that stores the number as the key and the value as the index. Then we can search through this map and see if the complement is in the map, and if it is and check if the complement's index is diffferent then we just return that index plus the index we are currently searching through.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for index, number in enumerate(nums):
            index_map[number] = index


        for index, number in enumerate(nums):
            complement = target - number

            if complement in index_map and index_map[complement] != index:
                return [index, index_map[complement]]


       

       


        

     

        
                

        