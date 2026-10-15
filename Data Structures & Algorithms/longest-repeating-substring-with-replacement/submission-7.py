class Solution:
    #  We can use the sliding window approach here, and we can have both left and right start at the beginning. Then we can check for how many replacements we need and see if thats equal to or under k. If it isn't then we have to shorten our window so that its valid for at most k replacements. We can do that by shrinking our window by moving our left pointer on and on until the length of the window - the highest frequnt letter is less than or equal to k. We are doing this because we are figuring out which ones to replace by finding how many to replace. 
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



        