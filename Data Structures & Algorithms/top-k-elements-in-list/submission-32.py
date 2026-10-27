
class Solution:
    # We can use the bucket sort approach here. So first we can make a frequency list to see which elements are the most frequent. Then we can make a bucket list and place a bucket for each element. Then we can basically set the indexes of that bucket list as the frequencies, and correspondingly insert the numbers at their frequency/index bucket. Then we can search through the bucket list, starting from the end as that would be the highest index or frequency. And then we can loop through that bucket, and insert the numbers to the result list. And we can keep checking if the length of that list equals k or not and if it does then we can return the list.

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for element in nums:
            freq_map[element] += 1
        
        buckets = []
        for element in range(len(nums) + 1):
            buckets.append([])

        for number, frequency in freq_map.items():
            buckets[frequency].append(number)

        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for number in buckets[i]:
                result.append(number)

                if len(result) == k:
                    return result

        