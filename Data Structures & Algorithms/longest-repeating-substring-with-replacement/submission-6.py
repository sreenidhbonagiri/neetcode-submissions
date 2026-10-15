class Solution:
    # Again can use the sliding window approach. So left to 0, and loop through until right reaches the end of the list. Can also have a running length character. Now we can create a frequency map and count how many times the letters appear. 
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        total_length = 0
        freq_map = defaultdict(int)

        for right in range(len(s)):
            freq_map[s[right]] += 1

            while (right - left + 1) - (max(freq_map.values())) > k:
                freq_map[s[left]] -= 1
                left += 1

            curr_length = right - left + 1
            total_length = max(total_length, curr_length)


        return total_length
            