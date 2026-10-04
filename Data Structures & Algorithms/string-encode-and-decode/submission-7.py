class Solution:
    #First we can combine the strings using join. And we can also make sure that we add a delimeter like # and with the length of the letters as before it. 
    def encode(self, strs: List[str]) -> str:
        parts = []

        for element in strs:
            parts.append(str(len(element)) + "#" + element)
        
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            j = i 

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]

            result.append(word)

            i = j + 1 + length

        return result





        
        




