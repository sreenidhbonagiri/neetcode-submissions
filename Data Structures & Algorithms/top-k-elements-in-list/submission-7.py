from collections import Counter
# So we can make a frequency map so we can have a count of how many times each letter has occured. Then, we can put each key value pair in a list into a new list called result. Then we can

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        result = []
        for number, freq in freq_map.items():
            result.append([freq,number])
        
        result.sort()

        i = 0
        final = []
        while i < k:
            final.append(result.pop()[1])
            i += 1

        return final


        
            


    


    

    


    
        

            

        



        