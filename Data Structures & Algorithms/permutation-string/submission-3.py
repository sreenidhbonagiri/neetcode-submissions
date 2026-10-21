class Solution:
    # We can use a sliding window approach here. We can build two frequency maps, one for s1 and one for s2. Then we can basically search through s2, and try to see if that frequency map from s1 can match s2. If it does, then we can return True if not return False. And as we are searching through s2, we have to make sure we are looking at 3 letters at a time or the length of the s1 frequency maps at a time. 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = defaultdict(int)
        s2_map = defaultdict(int)

        for letter in s1:
            s1_map[letter] += 1

        for letter in s2[:len(s1)]:
            s2_map[letter] += 1

        if s1_map == s2_map:
            return True

        left = 0
        
        for right in range(len(s1), len(s2)):
            s2_map[s2[left]] -= 1

            if s2_map[s2[left]] == 0:
                del s2_map[s2[left]]
            left += 1

            s2_map[s2[right]] += 1

            if s1_map == s2_map:
                return True

        return False



      

        