class Solution:
    from collections import Counter
    # Plan:
    # Could use counter to see if both the counters match then they are   anagrams.
    # 
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)