class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            _s = sorted(s)
            _t = sorted(t)
            if len(_s) != len(_t):
                return False
            for i in range(len(_s)):
                if _s[i] is not _t[i] or _t[i] is None:
                    return False
            return True
        