class Solution:
    from collections import Counter
    
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        else:
            return False