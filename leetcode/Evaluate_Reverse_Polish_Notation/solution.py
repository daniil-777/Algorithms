class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for el in tokens:
            if el not in operators:
                stack.append(int(el))
            elif el == '+':
                
                stack.append(stack.pop() + stack.pop())
            elif el == '-':
                stack.append(-stack.pop() + stack.pop())
            elif el == '*':
                stack.append(stack.pop() * stack.pop())
            elif el == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))            
                
            # print("stack: ", stack)
                
        return stack.pop()