class Solution:
    # Ok so for this we can make two frequency maps one for s1 and one for s2, but the one for s2 should only go up until the same length as s1. Then we can check if s1 and s2 are equal to begin with and if they are then we can return true right away. If not, we can loop through starting from the length of s1 up until the length of s2. Now we can get rid of our starting character from the frequency map by getting rid of left, then increment left so it points to our next character. Then we can add right to our map so we still have the same length of s1. And then we can compare this new map to s1 and check if they match, if so return true. If the whole loop goes through without returning then we can return false.

    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1_map = defaultdict(int)
        s2_map = defaultdict(int)

        for element in s1:
            s1_map[element] += 1

        for element in s2[:len(s1)]:
            s2_map[element] += 1

        if s1_map == s2_map:
            return True

        for right in range(len(s1), len(s2)):
            s2_map[s2[left]] -= 1
            if s2_map[s2[left]] == 0:
                del s2_map[s2[left]]

            left += 1
            s2_map[s2[right]] += 1

            if s1_map == s2_map:
                return True

        return False


       