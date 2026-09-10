class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for index, number in enumerate(nums):
            y = target - number

            if y in hash:
                return [hash[y], index]

            hash[number] = index
        
        return []
                

        