class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        total_length = 0

        for num in nums:
            if (num - 1) not in lookup:
                current = num
                curr_length = 1

                while current + 1 in lookup:
                    current += 1
                    curr_length += 1
                
                total_length = max(curr_length, total_length)

        return total_length



        