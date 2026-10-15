class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        target_map = defaultdict(int)
        curr_map = defaultdict(int)

        if len(s1) > len(s2):
            return False
        
        for num in s1:
            target_map[num] += 1

        for num in s2[:len(s1)]:
            curr_map[num] += 1

        if target_map == curr_map:
            return True

        for right in range(len(s1), len(s2)):
            curr_map[s2[left]] -= 1
            if curr_map[s2[left]] == 0:
                del curr_map[s2[left]]

            left += 1
            curr_map[s2[right]] += 1

            if target_map == curr_map:
                return True
        
        return False


                



                

        