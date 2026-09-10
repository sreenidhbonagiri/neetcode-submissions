class Solution:

    # Plan:
    # We could add a hashtag as a delimeter for between each word. We also need to keep track of the length of each word so that we will be able to decode each string individually.
    # So we can use the .join method to join the strings together, but in between each string we need to add the delimeter. Hello#World#Adad.
    # But what if the original string has the hashtags as part of the string and not as a delimeter?
    # Okay so what if the delimeters just had the a number which is the length of the string followed by a hashtag like 5#Hello5#World.
    # So I can loop through the list, and at each string element I can possibly do a .join with the length of the string and the hash in between.
    # 5#Hello5#World
    def encode(self, strs: List[str]) -> str:
        result = []
        for element in strs:
            result.append(str(len(element)) + "#" + element)
        
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = s.find('#', i)

            length = int(s[i:j])
        
            result.append(s[j + 1: j + 1 + length])
            
            i = j + 1 + length
        
        return result



