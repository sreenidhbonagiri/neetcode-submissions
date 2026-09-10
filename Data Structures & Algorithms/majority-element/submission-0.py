class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)
        target = len(nums) / 2
        for num in nums:
            freq_map[num] += 1

        for num in freq_map:
            if freq_map[num] > target:
                return num