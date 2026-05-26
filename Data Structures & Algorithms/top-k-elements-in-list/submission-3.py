class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = dict()
        for i in nums:
            if i not in res:
                res[i] = 0
            res[i]+=1
            
        out = dict()
        for key, val in res.items():
            if val not in out:
                out[val] = []
            out[val].append(key)

        _out = []
        key_s = sorted(out.keys())
        _k = k
        for i in range(len(key_s)-1, -1, -1):
            if _k == 0:
                break
            key = key_s[i]
            for j in out[key]:
                _out.append(j)
                _k-=1
                if _k == 0:
                    break
        
        return _out