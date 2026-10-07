class Solution:
    # We are going to change the entire nums into a set for easy lookup. Then we will search through the nums list and check only if nums[i] - 1 is not in the list then only we are going to continue. Then we can set a current variable equal to the element, then we will keep looping while until current + 1 is no longer in the set. Then for each loop we can increment our current + 1, and we can have a running sum and increment that as well. Once the current + 1 is not found in the list thats when we can stop, and compare the totals with the max. And then return the total.
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        total = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in lookup:
                current = nums[i]
                curr_total = 1

                while current + 1 in lookup:
                    current += 1
                    curr_total += 1

                total = max(curr_total, total)

        return total 




        