class Solution:
    # Okay so we can use two pointers here left and right. Set left and right both equal to 0. Then we can also have a running total variable and set that to 0. And we can also have a set to check for duplicates. Then we can loop through the list until right ends up being equal to the length of the list
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
            curr_length = right - left + 1
            total_length = max(total_length, curr_length)
            right += 1
            
        return total_length



