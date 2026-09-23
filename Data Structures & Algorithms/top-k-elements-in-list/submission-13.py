from collections import Counter
# We can make a frequency map containing the number as the key and the values as the frequencies.
# Then we can invert his map so that the keys are actually the frequencies and the values are the numbers.
# Then we can take all of the keys and put them in a list and then sort that list so the most frequent are at the top.
# Then we can loop through that list starting from the end and decremnting, and then just returning the values of those keys and keep doing it k number of times.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        invert_map = {}
        for key, value in freq_map.items():
            if value not in invert_map:
                invert_map[value] = []
            
            invert_map[value].append(key)

        temp = []
        for key in invert_map:
            temp.append(key)
        temp.sort()

        result = []
        for i in range(len(temp) - 1, -1, -1):
            frequency = temp[i]

            for number in invert_map[frequency]:
                result.append(number)

            if len(result) == k:
                return result
        

    
        
        




        
            


    


    

    


    
        

            

        



        