class Solution:
    # I think we can go through the list and keep track of both the number and index using enumerate. Then for each number subtract it from the target to find the other number we need to make it happen. And find the other number in the list and keep track of its index and number too. And then just gotta return both indixes and we can sort it when returning it.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        
        for index, number in enumerate(nums):
            index_map[number] = index

        for index, num in enumerate(nums):
            complement = target - num

            if  complement in index_map and index_map[complement] != index:
                return [index, index_map[complement]]
                
        

     

        
                

        