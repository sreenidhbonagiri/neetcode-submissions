#
class Solution:
    # We can use two pointers left and right. Left starts and right starts at the end. We also have to check for case sensitivity and alphanumerical characters. After we done that, we can loop till the pointers meet and keep checking at every iteration if the left pointers and right pointers donte match, and if it any point they dont match, then we return false right away. If gets through that if statement then we can keep looping until the end and if goes through that entire loop without returning false we can safely return true.
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
    