# Have one pointer point on the left side and one point to the right side. If the pointers equal the same letter then keep moving inward and inward. At any point if they don't match then return False. But if they make it inward so much to the point where they both point towards each other, then return True. And make sure to join the string before traversing.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""

        for character in s:
            if character.isalnum():
                new += character.lower()

        left = 0
        right = len(new) - 1

        while left < right:
            if new[left] != new[right]:
                return False
            
            left += 1
            right -=1 

        return True

            



        