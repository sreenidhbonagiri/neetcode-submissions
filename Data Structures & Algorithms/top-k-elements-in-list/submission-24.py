# We can first create a frequency map to collect the frequencies for each number. Then we can create a new map that holds the frequency as the key, and the value would be a list containing all of the numbers with that frequency. Then we can create a temporary list and append all of the keys which are the frequencies into that list. Then sort that list so that it goes from lowest to highest. Then loop through that list from the end to the beginning so it gets the highest first. And then we access first element's value which would be that list of numbers and then loop through taht list of numbers to add them into a result list. And keep adding until that length of the result list equals to k. 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])

        for number, frequency in freq_map.items():
            buckets[frequency].append(number)

        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for number in buckets[i]:
                result.append(number)

                if len(result) == k:
                    return result