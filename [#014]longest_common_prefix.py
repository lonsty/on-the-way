class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_, max_, i = min(strs), max(strs), 0
        
        for _ in range(min(len(min_), len(max_) + 1)):
            if min_[i] != max_[i]:
                break
            i += 1

        return min_[:i]
