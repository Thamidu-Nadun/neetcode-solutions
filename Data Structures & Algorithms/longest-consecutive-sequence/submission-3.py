class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_n = 0
        if len(nums) == 0:
            return max_n

        sort_n = sorted(list(set(nums)))
        res = defaultdict(list)
        
        idx = 0
        prev = sort_n[0]
        res[idx].append(prev)
        for i in range(1, len(sort_n)):
            _next = prev+1
            if _next == sort_n[i]:
                res[idx].append(sort_n[i])
                prev = sort_n[i]
            else:
                idx = idx + 1
                prev = sort_n[i]
                res[idx].append(prev)
        
        for i in res.values():
            n = len(i)
            max_n = max(max_n, n)
            
        return max_n
            
        