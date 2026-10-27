class Solution:
    # We can use a stack to push the opening brackets, then when it gets to a closing bracket, we need to check if the element at the top of the stack is the right opening bracket and if it is we can pop both and continue, if not we need to return false right away. If the whole stack is popped at the end only then we can return true.

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

        return stack == []
