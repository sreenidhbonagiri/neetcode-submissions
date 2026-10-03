from collections import Counter

class Solution:
    # We want to search through all of the strings and basically sort each one. After sorting the element then check if the sorted version is in the hash map or not. If its not then we can create a new key for that and set the value equal to an empty list. But if the sorted version is already in the map, then we can add the original elemenet to the map as a value. Then we can invert the map so that the key is the list with the original elements. And then we can make a new result list and append each key to that list. 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for element in strs:
            sort = "".join(sorted(element))

            if sort not in hash_map:
                hash_map[sort] = []

            hash_map[sort].append(element)

        result = []

        for value in hash_map.values():
            result.append(value)

        return result

       
        




        
    

        

        