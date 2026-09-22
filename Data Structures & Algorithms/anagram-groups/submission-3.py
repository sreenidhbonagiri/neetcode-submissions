from collections import Counter

class Solution:
    # First we can make a map that has sorted one word as the key and its anagrams as the values. Then we can loop through the map and for each key we can append its values in a list format to another list and keep going till we countered every key. And if there is only one element in the list then we can just return that element in a listed list format.
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for element in strs:
            key = "".join(sorted(element))
            if key not in anagram_map:
                anagram_map[key] = []
            
            anagram_map[key].append(element)
        
        result = []
        for element in anagram_map:
            result.append(anagram_map[element])

        return result



        
    

        

        