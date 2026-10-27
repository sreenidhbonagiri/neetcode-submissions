class Solution:
    # For this problem we can use sliding window. So we can first create two frequency maps one for s1 and one for s2 though the map for s2 should be the same length as the one for s1. Then check if the two match, if they do then return true. If not, then we can loop through until right reaches the end of s2 map starting from after the length of the first map. Then each iteration, we can get rid of our first letter in the s2 map, and add another letter to the end of the s2 map. And then check if this new map is equal to s1 map, if so then return true, other wise keep looping until right hits the end of the list. And if goes through the entire list without returning true then we can return false.
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1_map = defaultdict(int)
        s2_map = defaultdict(int)

        for letter in s1:
            s1_map[letter] += 1

        for letter in s2[:len(s1)]:
            s2_map[letter] += 1

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

            


            

       