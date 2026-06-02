class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            curr = temperatures[i]
            stack = []
            for j in range(i+1, len(temperatures)):
                _next = temperatures[j]
                if _next > curr:
                    stack.append(_next)
                    break
                stack.append(_next)
                
            if stack:
                max_n = max(stack)
                if max_n > curr:
                    res.append(len(stack))
                else:
                    res.append(0)
            else:
                res.append(0)
        
        return res