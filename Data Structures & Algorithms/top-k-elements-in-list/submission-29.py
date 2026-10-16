# We can use bucket sort here. So first we can create a frequency map. Then we can create a bucket list so basically we know any specific number can only repeat len(nums) times right. So we can use indexes as the frequency count. So for each index, we can have a list or bucket that holds the numbers. So now, we need to use the frequency map to correctly place each key or number to its correct bucket using its value.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])

        for number, freq in freq_map.items():
            buckets[freq].append(number)

        result = []

        for i in range(len(buckets) - 1, -1, -1):
            for number in buckets[i]:
                result.append(number)

            if len(result) == k:
                return result

            
        

        

        

     