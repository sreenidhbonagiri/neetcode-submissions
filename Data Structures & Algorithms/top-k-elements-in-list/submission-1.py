from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #while until a variable equals k and inside the while the variable would just keep incrementing

        hash = {}
        for element in nums:
            if element not in hash:
                hash[element] = 1
            else:
                hash[element] += 1

        bucket = []
        for element in range(len(nums) + 1):
            bucket.append([])
        
        for element, counter in hash.items():
            bucket[counter].append(element)
        
        output = []
        for element in range(len(bucket) - 1, -1, -1):
            for number in bucket[element]:
                output.append(number)
                if len(output) == k:
                    return output
        




        