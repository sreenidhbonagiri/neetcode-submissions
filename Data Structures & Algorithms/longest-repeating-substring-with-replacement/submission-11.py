class Solution:
    #  We can use sliding window approach here. So we can have our left pointer, and then can also initalize a frequency map to know which letters are the most common. Then we can go through the string, an as we go through the string we can increment our map based on what we see. Then we can calculate the amount of replacements that we need by calculating the window length, and subtracting the window with the frequency of the most common letter. This gives us the amount of letters needed to replace to make everything one distinct character. Then we can check if this replacement number is less than or equal to k, and if it is then length of the window. If not, then we can use sliding window approach by decrementing our left value from the frequency map, and then adding another right to the frequency map to the end. Then loop again.
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
            total_length = max(total_length, curr_length)

        return total_length





       