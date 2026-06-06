class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ("+", "-", "/", "*")
        
        for token in tokens:

            if token in op:
                b = int(stack.pop())
                a = int(stack.pop())
                match token:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":
                        stack.append(a * b)
                    case "/":
                        stack.append(a / b)
            else: 
                stack.append(int(token))
        return int(stack[0])

        