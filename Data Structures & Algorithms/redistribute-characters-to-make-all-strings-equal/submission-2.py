from collections import Counter
class Solution:
    # Basically make a frequency map that has the frequencies of each letter in all of the words
    # Then we can check if the frequencies of each letter have a remainder, and if they do then that would mean that are more or less frequency count for that specific character than there are number of words which would mena that every string would not be equal as some may have more of the letter than other words. 
    # But if the remainder is 0, then that would mean each letter has the same frequency as the number of words which would make the words equal only if every letter frequency is the same as the number of words.
    def makeEqual(self, words: List[str]) -> bool:
        freq_map = defaultdict(int)
        n = len(words)

        for word in words:
            for character in word:
                freq_map[character] += 1

        for character in freq_map:
            if freq_map[character] % n:
                return False
        
        return True

        



