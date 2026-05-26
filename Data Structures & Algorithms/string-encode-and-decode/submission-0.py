class Solution:

    def encode(self, strs: List[str]) -> str:
        KEY = '2'
        out = ""
        for i in strs:
            for j in i:
                out += chr(ord(j) ^ ord(KEY))
            out+='%20%'
        return out

    def decode(self, s: str) -> List[str]:
        KEY = '2'
        strs = s.split('%20%')
        strs.pop()
        out = []
        for i in strs:
            _s = ''
            for j in i:
                _s += chr(ord(j) ^ ord(KEY))
            out.append(_s)
        return out