class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            days = 0
            found = False
            for j in range(i+1, len(temperatures)):
                days += 1
                if temperatures[j] > temperatures[i]:
                    res.append(days)
                    found = True
                    break
            if not found:
                res.append(0)
                
        return res