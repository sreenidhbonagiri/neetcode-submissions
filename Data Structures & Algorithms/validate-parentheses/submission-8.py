class Solution:
    # For this we can create a dictionary with the keys as the closing brackets and the values as the opening brackets. Then we can search through s, and if the element is a value in the dictionary, then we can append it to the stack. Then we can check if the element is a key in the dictionary, if so, then we can first check if there even is an opening bracket for it or if the stack is empty, if it is empty then we can return false right away. Otherwise, we can check if the value of that element's key is in the top of the stack or not, and if it is then we can just pop that element. If not return false. If it goes through the entire loop without returning false, we can check at the end if the stack is empty, and if so then we can return true.

    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')' : '(', '}' : '{', ']' : '['}

        for element in s:
            if element in bracket_map.values():
                stack.append(element)

            elif element in bracket_map:
                if stack == []:
                    return False
                
                if stack[-1] == bracket_map[element]:
                    stack.pop()
                else:
                    return False
        
        if stack == []:
            return True
        else:
            return False


       