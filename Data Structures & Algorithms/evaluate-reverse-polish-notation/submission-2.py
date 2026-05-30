class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in '+-*/':
                r = stack.pop()
                l = stack.pop()
                res = int(l)
                if i == '+':
                    res += int(r)
                elif i == '-':
                    res -= int(r)
                elif i == '*':
                    res *= int(r)
                elif i == '/':
                    res /= int(r)
                stack.append(res)
            else:
                stack.append(i)
        return int(stack.pop()) if len(stack) == 1 else int(tokens.pop())