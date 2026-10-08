class Solution:
    # So we can have two pointers one that starts at the first letter and the other goes on to the rest of the string. And each time the right moves on, we can check if its equal to the left pointer or not, and if its not then we can increment our counter. But if it is equal, then we set our left equal to our right and we just move our right and do the same thing again and reset the count.
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        lookup = set()
        total_length = 0

        while right < len(s):
            while s[right] in lookup:
                lookup.remove(s[left])
                left += 1
            

            lookup.add(s[right])
            max_length = right - left + 1
            total_length = max(total_length, max_length)

            right += 1

        return total_length

            



