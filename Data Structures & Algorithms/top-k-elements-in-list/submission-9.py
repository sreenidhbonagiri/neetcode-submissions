from collections import Counter
# Could make a frequency map which helps you see the most frequent ones. And then we can somehow gather the highest values, and put their keys in a list ranked from most frequent to least. And then we can keep appending the first or last element whatever is the highest into a result list and keep doing that k times. 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        new_map = {}
        for key, value in freq_map.items():
            if value not in new_map:
                new_map[value] = []

            new_map[value].append(key)

        bank = []
        for key in new_map:
            bank.append(key)

        bank.sort()
        result = []

        for i in range(len(bank) - 1, -1, -1):
            freq = bank[i]

            for num in new_map[freq]:
                result.append(num)

            if len(result) == k:
                return result
        
        




        
            


    


    

    


    
        

            

        



        