class Solution:
    # We can encode the strings by adding a delimeter before the word, and before the delimeter can add the length of the word so it can make it easy for decoding.
    def encode(self, strs: List[str]) -> str:
        result = []
        for element in strs:
            result.append(str(len(element)) + "#" + element)
        
        return "".join(result)
        

    # Then we can decode it by having two pointers i and j. Have our result list. And have a loop until i < len(s), and then set a j pointer. Set the j pointer equal to i since it will start from i. Then it will keep going until it hits a # delimeter. At that point we can set the length equal to a splice between i and j. Then we can set our word equal to a splice between j + 1 which would be the first letter of the wrod untl j + 1 + length which would point towards the number for the length of the next word but since splice doesnt count that but counts - 1 it would work. And then set i equal to j + 1 + length which would start the next word. And also append that word to the result list and keep looping that until i goes to the end of the string.
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