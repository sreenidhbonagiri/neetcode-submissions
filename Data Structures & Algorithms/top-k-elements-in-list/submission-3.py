from collections import Counter
# Make a frequency map, then sort the values from the highest to least into a list but also make sure you have the keys, and then we can make it so that it returns the highest number k times, and once it returns the highest number it would get removed from the list, and then the process would continue until k is done.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        array = []
        for number, frequency in freq.items():
            array.append([frequency, number])
        array.sort()

        result = []
        while len(result) < k:
            result.append(array.pop()[1])

        return result 

    


    

    


    
        

            

        



        