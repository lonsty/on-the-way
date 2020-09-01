import re

class Solution:
    v = {'I': '+1', 'V': '+5', 'X': '+10', 'L': '+50', 'C': '+100', 'D': '+500', 'M': '+1000'}
    p = re.compile(r'(I[V|X])|(X[L|C])|(C[D|M])')
    
    def romanToInt(self, s: str) -> int:
        s = self.p.sub(r'-\1\2\3', s)
        for c in self.v:
            s = s.replace(c, self.v.get(c, c))
        return eval(s)
