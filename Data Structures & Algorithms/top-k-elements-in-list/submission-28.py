# We can first make a frequency list. Then we can make a list called buckets and and a list to each number of items in the list. Then we can set the numbers with a certain frequency at a certain index in that bucket list basically correlating the indexes and frequencies cause a number can at most have a frequency of the length of the list. And then we can make a result list. And we can loop through the bucket list from the end to the beginning, and add the elements in each bucket to the result list. And keep checking the length of the result list and whenever that equals k thats when we will return the result list.
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

            
        