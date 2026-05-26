class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()
        checked = set()
        _len = len(strs)
        for i in range(_len):
            key = strs[i]
            if key in checked:
                continue
            seen[key] = [key]
            for j in range(i+1, _len):
                target = strs[j]
                if len(key) != len(target):
                    continue
                key_s = sorted(key)
                target_s = sorted(target)
                if key_s != target_s:
                    continue
                seen[key].append(target)
                checked.add(target)
        return list(seen.values())
        