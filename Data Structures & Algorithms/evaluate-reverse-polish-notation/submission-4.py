class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                

                if token == "+":
                    new = left + right
                elif token == "-":
                    new = left - right
                elif token == "*":
                    new = left * right
                elif token == "/":
                    new = int(left / right)

                stack.append(new)

        return stack.pop()
        
                
            
        
        

            