class Solution:
    # We can first make the nums list a set for faster look up times. Then we can go through each element of nums and check whether that number - 1 is not in the list. And if its not then that would be our starter. Also have a longest variable. And then we gotta keep checking if that current number + 1 is in the list or not using a while current + 1 is still in the set. And for each iteration we set current = current + 1 and set a length variable and keep incrementing it so that we can keep track of how long it is. And then we take the maximum of the length and the longest and thats what we set longest to. And then at the end just return the longest variable.
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in lookup:
                current = num
                length = 1
                while current + 1 in lookup:
                    current = current + 1
                    length += 1
                longest = max(length, longest)
           

        return longest