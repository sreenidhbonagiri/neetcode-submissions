# We can have two pointers left and right. We can have left equal to 0 and right equal to the length of the string - 1. Then we while loop until the left < right isnt true anymore. Then we check if at any point the left and right arent equal we can return False right away, and keep incrementing the left pointer and keep decrementing the right pointer. If it passes the entire while loop without returning false at any point then we can return True. Also gotta create a new string containing only alphanumeric characterss.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for char in s:
            if char.isalnum():
                new += char.lower()

        left = 0
        right = len(new) - 1

        while left < right:
            if new[left] != new[right]:
                return False

            left += 1
            right -= 1
            
        return True


        

