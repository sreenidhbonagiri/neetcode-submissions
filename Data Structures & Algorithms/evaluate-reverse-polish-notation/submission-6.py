class Solution:
    # Okay so we can create a stack list, and then we can loop through tokens and for each token we can check whether its an integer or a symbol. If it's an integer, only then can we append it to the stack. If it's a symbol, then we have to 
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        new = 0

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(token)
            else:
                right = int(stack.pop())
                left = int(stack.pop())

                if token == "+":
                    new = left + right
                    stack.append(new)
                elif token == "-":
                    new = left - right
                    stack.append(new)
                elif token == "*":
                    new = left * right
                    stack.append(new)
                elif token == "/":
                    new = int(left / right)
                    stack.append(new)

        return int(stack.pop())

        