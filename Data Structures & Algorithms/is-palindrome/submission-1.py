# Have two pointers left and right where left starts it and right starts at the end. And just keep looping until i becomes the length of the string s. And then keep checking if they dont equal each other at any point return false. And increment left and decrement right. And if it goes through without returning false then return true. Also need to ignore non-alphanumeric numbers.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for element in s:
            if element.isalnum():
                new += element.lower()

        left = 0
        right = len(new) - 1
        while left < right:
            if new[left] != new[right]:
                return False

            left += 1
            right -= 1

        return True

