class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opStack = []

        for c in tokens:
            if c == "+":
                opStack.append(opStack.pop() + opStack.pop())
            elif c == "-":
                a, b = opStack.pop(), opStack.pop()
                opStack.append(b - a)
            elif c == "*":
                opStack.append(opStack.pop() * opStack.pop())
            elif c == "/":
                a, b = opStack.pop(), opStack.pop()
                opStack.append(int(float(b) / a))
            else:
                opStack.append(int(c))
        return opStack[0] 
            
