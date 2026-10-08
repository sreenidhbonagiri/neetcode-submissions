class Solution:
    # So we can use two pointers here, left and right that both start at 0. We can also have a running count of the length and set that to 0 as well. And we can also have a set to track letters that we have already seen. So for each letter, we can add that letter to the set, and we can keep our left at the start, and keep incrementing right until we see a duplicate value. 
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        total_length = 0
        seen = set()

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            length = right - left + 1
            total_length = max(total_length, length)
            right += 1

        return total_length





            
        