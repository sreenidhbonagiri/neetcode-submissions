
class Solution:
    # Okay we need to use the bucket sort approach. So first we can create our frequency map. Then we can create our bucket list and make our buckets. Then we can put in our keys to the corresponding bucket by making the indexes equal to the frequency count which is the values.
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



        

        
       
        

        

     