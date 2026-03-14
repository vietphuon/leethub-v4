class Solution:
    def minDeletions(self, s: str) -> int:
        hs = {}
        for c in s:
            if c not in hs:
                hs[c] = 0
            hs[c] += 1
        
        seen = {}
        res = 0

        for c in s:
            if c in seen:
                pass
            else:
                while hs[c] > 0 and hs[c] in seen.values():
                    hs[c] -= 1
                    res += 1
                
                seen[c] = hs[c]       
        return res
