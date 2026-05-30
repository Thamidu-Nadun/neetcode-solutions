class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        tags = {'}': '{', ']':'[', ')':'('}
        for i in s:
            if i in ['{', '[', '(']:
                stack.append(i)
            elif i in ['}', ']', ')']:
                if not stack or tags[i] != stack.pop():
                    return False
        return len(stack) == 0