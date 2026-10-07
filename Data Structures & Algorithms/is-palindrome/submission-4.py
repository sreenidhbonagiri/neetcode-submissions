# For this we can have two pointers left and right. And we keep looping as long as left < right, and at each iteration we can check if s[left] != s[right] at any point we can return false right away. But if not we can increment our left and right pointers. And if it goes through the entire loop without returning false we can return true at the end
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for element in s:
            if element.isalnum():
                new_s += element.lower()

        left = 0 
        right = len(new_s) - 1
            
        while left < right:
            if new_s[left] != new_s[right]:
                return False

            left += 1
            right -=1 

        return True
        