class Solution:
    # For this we can go through each element in the list and check if that element - 1 is in the list or not. If not then we can set that element to the current number, and also 
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        total = 0
        for element in nums:
            if element - 1 not in seen:
                curr = element 
                running = 1

                while curr + 1 in seen:
                    curr += 1
                    running += 1
                
                total = max(running, total)

        return total


        