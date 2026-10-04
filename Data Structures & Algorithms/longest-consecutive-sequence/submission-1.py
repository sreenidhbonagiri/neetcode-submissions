class Solution:
    # I think for each element in the list we should check if the element - 1 is also in this list. So make a set and add every number into that set. Then look up if that element - 1 is in the set and do that for every element until you find one that is not. That element will be the starting number. Then from that number on we can add 1 to the number and check if that element is in the string and if it is then add that to a list. Then check if the next element + 1 is in the list and if it is then add that to the list as well. And keep adding until its done and then return the length of that list.
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

                longest = max(longest, length)

        return longest



            




       