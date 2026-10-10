class Solution:
    # We want two pointers left and right. We want both of them to stay at 0. Left will for sure stay at 0 and right will move through all the characters in the string. Then for each element we add the letter to a frequency map. 
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq_map = defaultdict(int)
        total_length = 0

        for right in range(len(s)):
            freq_map[s[right]] += 1

            while (right - left + 1) - max(freq_map.values()) > k:
                freq_map[s[left]] -= 1
                left += 1

            curr_length = right - left + 1
            total_length = max(curr_length, total_length)

        return total_length

                



       
