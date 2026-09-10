class Solution:
    #We can go through the list and check to see if that numbers - 1 exists, if it does then we can go to that number and check if that numbers - 1 exists and keep going until it doesnt exist. Then that last number would be set to start the consecutive, and then we can just make another loop that adds the + 1 of that first number to the list until that + 1 doesnt exist and then just return that list.
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) 
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1

                while (num + length) in numSet:
                    length += 1
                
                longest = max(longest, length)
                
        

        return longest


        