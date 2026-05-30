class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        tags = {'}': '{', ']':'[', ')':'('}
        for i in s:
            if i in tags.values():
                stack.append(i)
            elif i in tags:
                if not stack or tags[i] != stack.pop():
                    return False
        return len(stack) == 0