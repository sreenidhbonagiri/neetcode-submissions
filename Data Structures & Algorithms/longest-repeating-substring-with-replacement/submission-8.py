class Solution:
    #  We can use the sliding window approach and have two pointers left and right. Left starts at 0, and we can have a running total length variable. We can also have a frequency map. Basically we are trying to find the window length - most frequent letter, and that would be the amount of replacements we would have to do. And we can loop until that is less than or equal to k. In that loop we can keep removing left and move our window until that condition gets satisfied.
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        total_length = 0
        freq_map = defaultdict(int)

        for right in range(len(s)):
            freq_map[s[right]] += 1

            while (right - left + 1) - (max(freq_map.values())) > k:
                freq_map[s[left]] -= 1
                left += 1

            curr_total = right - left + 1
            total_length = max(curr_total, total_length)

        return total_length

        

            




        