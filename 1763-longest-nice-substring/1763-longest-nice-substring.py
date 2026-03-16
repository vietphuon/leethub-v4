class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        
        chars = set(s)

        for idx, char in enumerate(s):
            if char.swapcase() not in chars:
                left = self.longestNiceSubstring(s[:idx])
                right = self.longestNiceSubstring(s[idx+1:])
                return max(left, right, key=len)
        
        return s
        
        # def is_nice(s: str):
        #     chars = set(s)
        #     for char in s:
        #         if char.upper() not in chars or char.lower() not in chars:
        #             return False
        #     return True
        # n = len(s)
        # res = ""
        # for left in range(n):
        #     for right in range(left + 1, n):
        #         sub_str = s[left:right+1]

        #         if is_nice(sub_str):
        #             if len(sub_str) > len(res):
        #                 res = sub_str
        
        # return res