class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            # base case: pattern exhausted
            if j == len(p):
                return i == len(s)
            
            first_match = i < len(s) and p[j] in (s[i], '.')
            
            if j + 1 < len(p) and p[j+1] == '*':
                # two choices:
                # 1) skip "x*" entirely (zero occurrences)
                # 2) use one occurrence — only if first_match
                res = dp(i, j+2) or (first_match and dp(i+1, j))
            else:
                # no '*', must match current char then advance both
                res = first_match and dp(i+1, j+1)
            
            memo[(i, j)] = res
            return res
        
        return dp(0, 0)