class Solution:
    # 
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        total_length = 0

        for number in nums:
            if number - 1 not in lookup:
                current = number
                curr_length = 1

                while current + 1 in lookup:
                    current += 1
                    curr_length += 1

                total_length = max(total_length, curr_length)

        return total_length





        