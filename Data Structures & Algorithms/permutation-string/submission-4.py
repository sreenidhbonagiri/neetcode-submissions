class Solution:
    # We can use the sliding window approach, so we can first calculate the frequency map for the first string. Then we can calculate the frequency map only up until the same length as string 1 for s2. And then we can first check if the two frequency maps match or not. If not then we can loop through starting from after the length of the first string until the end of the second string. And each time we can check if the frequency maps match or not, and each time we need to remove our first letter and add a letter to the end and then check. 
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
    


      

        