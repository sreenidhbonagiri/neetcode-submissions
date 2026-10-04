from collections import Counter
# We can create a frequency map to store the numbers as the key and its frequencies as the values.
# Then we can create a new map where we invert the values and the keys, and basically the numbers with the same frequencies go in a list and that list will be the key. So the key would be the single frequency count and the value would be a list containing the numbers that all have that same frequency. Then you create a temp list and put all of the keys in that list. And then you sort that list so it goes from least to greatest. And then you loop through that list starting from the end (highest) and make your way down. And as you are going through it each element you access its value list and append the numbers in that list to a result list. You go one by one and you keep checking if the result list length equals k, and when it does thats when you return the result list.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1

        new_map = {}

        for number, frequency in freq_map.items():
            if frequency not in new_map:
                new_map[frequency] = []

            new_map[frequency].append(number)

        temp = []
        for frequency in new_map:
            temp.append(frequency)

        temp.sort()

        result = []
        for i in range(len(temp) - 1, -1, -1):

            for number in new_map[temp[i]]:
                result.append(number)

                if len(result) == k:
                    return result
        
       