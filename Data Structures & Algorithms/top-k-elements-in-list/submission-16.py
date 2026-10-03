from collections import Counter
# Make a frequency map with the keys as the number and the values as the frequency. Then invert that map so that the frequencies are the keys and the numbers are the values. Then append all of those keys(frequencies) into a list. Then sort that list so it goes from lowest to highest. Then loop through that list starting from the end and make your way down. Then for each element append its value which is the actual number into a result list. And then check if the length of that result list is equal to k and when it is then return result.
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

        temp = []
        for key in new_map:
            temp.append(key)

        temp.sort()
        result = []
        for i in range(len(temp) - 1, -1, -1):
            for number in new_map[temp[i]]:
                result.append(number)

                if len(result) == k:
                    return result
        

        
            


    


    

    


    
        

            

        



        