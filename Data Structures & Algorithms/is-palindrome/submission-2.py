import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = re.sub(r'[^a-z0-9]', '', s.lower())
        for i in range(len(res)):
            l, r = i, len(res)-1-i
            if res[l] != res[r]:
                return False
        return True