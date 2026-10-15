class Solution:
    # We can use sliding window approach. So we can have two pointers left and right which both start at the beginning. Then we can also make a running length sum. Then we can loop as right goes through every element in the string. Then we can also have a set that holds the letters that we have already seen. Then we can have a while loop where as long as there is a duplicate, we can remove the letter from the set, and move the left pointer. Otherwise, if there is no duplicates, then we can add the letter to the set, we can move our right pointer forward, and increment our running total and compare and set the max.
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        total_length = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            window_length = right - left + 1
            total_length = max(total_length, window_length)
            right += 1

        return total_length

        

        



