class Solution:
    @staticmethod
    def isMapping(bl, br):
        return br == {'(': ')', '{': '}', '[': ']'}.get(bl)
    
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        
        brackets = []
        
        for c in s:
            if not brackets:
                brackets.append(c)
            else:
                if self.isMapping(brackets[-1], c):
                    brackets.pop()
                else:
                    brackets.append(c)
        return len(brackets) == 0
