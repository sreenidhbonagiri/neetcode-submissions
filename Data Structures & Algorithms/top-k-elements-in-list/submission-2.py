from collections import Counter
class Solution:
    # Plan:
    # We can first make a frequency map
    # Then we can search through each element of the nums array and create a bucket for each number in a new list which will hold the the numbers in its corresponding indexed bucket 
    # Then we can fill in the frequency map dictionary where the key is the number and the values are the frequencies
    # Then we can go through this frequency map and put the numbers in the corresponding index buckets depending on their frequencies given by their values.
    # Now that we have the bucket list filled out, then we can return the k most frequent elements by going through this list from the end to the start cause the highest index is the end. 
    # And we can put the number in the highest index bucket and append it to a result list
    # And we can loop this so it keeps going until the result list is as long as k is.
    #Then we can return this result list

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        bucket = []
        for i in range(len(nums) + 1): 
            bucket.append([])
        
        for element in nums:
            if element in freq_map:
                freq_map[element] = 1 + freq_map.get(element, 0) 
            else:
                freq_map[element] = 1

        for number, count in freq_map.items():
            bucket[count].append(number)
        
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for element in bucket[i]:
                result.append(element)
            
            if len(result) == k:
                return result

        

            

        



        