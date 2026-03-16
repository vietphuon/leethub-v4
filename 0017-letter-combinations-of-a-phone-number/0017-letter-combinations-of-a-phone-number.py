class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hs = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        n = len(digits)
        arr = []
        def dfs(idx=0, curr=''):
            if idx == n:
                arr.append(curr)
                return

            for c in hs[digits[idx]]:
                dfs(idx + 1, curr + c)
        dfs()
        return arr

    def letterCombinations_2(self, digits: str) -> List[str]:
        hs = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': 'wxyz',
        }
        n = len(digits)
        if n == 1:
            return [i for i in hs[digits[0]]]
        if n == 2:
            return [i + j for i in hs[digits[0]] for j in hs[digits[1]]]
        if n == 3:
            return [i + j + k for i in hs[digits[0]] for j in hs[digits[1]] for k in hs[digits[2]]]
        if n == 4:
            return [i + j + k + l for i in hs[digits[0]] for j in hs[digits[1]] for k in hs[digits[2]] for l in hs[digits[3]]]