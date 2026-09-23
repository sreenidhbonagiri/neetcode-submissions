from collections import Counter

class Solution:
    # Make a signature for the anagrams as the key to a map and its value would be a list containing all of the strings that correlate to the signature. Then return a list appending those values to the list.
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for element in strs:
            key = "".join(sorted(element))

            if key not in map:
                map[key] = []
            
            map[key].append(element)

        
        result = []

        for key, value in map.items():
            result.append(value)

        return result

                

        




        
    

        

        