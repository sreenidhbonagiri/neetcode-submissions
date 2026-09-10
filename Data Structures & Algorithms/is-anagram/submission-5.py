from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s = Counter(s)
        counter_t = Counter(t)

        if counter_s == counter_t:
            return True
        else:
            return False

        

        