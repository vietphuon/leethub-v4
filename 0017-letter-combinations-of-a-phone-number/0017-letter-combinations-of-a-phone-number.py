class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hs = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        arr = []
        def dfs(idx=0, curr=""):
            if len(curr) == len(digits):
                arr.append(curr)
                return

            for c in hs[digits[idx]]:
                dfs(idx+1, curr + c)
        
        dfs()
        return arr