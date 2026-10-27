class Solution:
    # What I want to do here, is the sliding window approach. So first I will have a left pointer at the beginning, and have a total length counter variable. I will also initialize a frequency map to hold the counts of the most frequent letters. Then I will loop through until right hits the end of the list, and each iteration, I will modify the frequency map. Then check how many replacements are needed by subtracting the current window length by the frequency of the most frequent letter from the map. This will give us how many replacements we need to make, and if that number is more than k, then we will get rid of our left pointed value from our frequency map, increment left so it points to the next character, and then add our right to the map as well. But if the replacements is less than or equal to k, then we can update our total length variable, and then lastly will just return that total length variable.
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        total_length = 0
        freq_map = defaultdict(int)

        for right in range(len(s)):
            freq_map[s[right]] += 1

            while (right - left + 1) - max(freq_map.values()) > k:
                freq_map[s[left]] -= 1
                left += 1
            
            curr_length = right - left + 1
            total_length = max(total_length, curr_length)

        return total_length