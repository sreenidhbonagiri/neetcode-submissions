class Solution:
    # We can firste encode the string by creating a new list. Then for each element in the list, we can append the length of the element + the delimeter # + the element itself. And do that for each element and then at the end join them into 1 string and return that.
    def encode(self, strs: List[str]) -> str:
        result = []
        for element in strs:
            result.append(str(len(element)) + "#" + element)
        
        return "".join(result)

    # Now to decode we can create a result list then we can set two pointers i and j. So we can set i to 0 to start off and then we can create a while loop that keeps going until i is greater than the length of the result. Then we can set j equal to i to begin with, then we can have another while loop that goes until j points to the delimeter. Then we can set the length equal to a split from i to j. Then we can set the word equal to from j + 1 to j + 1 + length. Then we can set i equal to j + 1 + length. And append te word to the result list. 
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word = s[j + 1: j + 1 + length]
            result.append(word)

            i = j + 1 + length

        return result
        