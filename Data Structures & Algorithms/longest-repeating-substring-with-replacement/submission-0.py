class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq_map = defaultdict(int)
        max_length = 0
        
        for right in range(len(s)):
            char = s[right]
            freq_map[char] += 1
            window_length = right - left + 1
            highest_freq = max(freq_map.values())
            replacements = window_length - highest_freq

            while (right - left + 1) - max(freq_map.values()) > k:
                freq_map[s[left]] -= 1
                left += 1
                
            curr_length = right - left + 1
            max_length = max(max_length, curr_length)


        return max_length
            



