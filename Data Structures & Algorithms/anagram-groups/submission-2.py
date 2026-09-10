from collections import Counter
# Plan:
# Could sort each of the elements in the list, and then join them back together to have a nice string
# Then you can make the sorted version the key and the value can be a list that holds all of the anagrams of that sorted version.
# Then all of you have to do is just return the values of this dict and return it in a list format
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for element in strs:
            sorted_element = "".join(sorted(element))

            if sorted_element in hash:
                hash[sorted_element].append(element)
            elif sorted_element not in hash:
                hash[sorted_element] = [element]
        
        return list(hash.values())

        

        