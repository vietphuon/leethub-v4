class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        if n == 0:
            return 0
        self.res = 0
        
        def dfs(idx=0, curr=''):

            c = set(curr)
            if len(c) != len(curr) and curr: # sub-string contain duplicate char
                return
            
            # print(f"Good ss: {curr}")
            if len(curr) > self.res:
                self.res = len(curr)

            for i, ss in enumerate(arr[idx:]):
                dfs(idx + i, curr + ss)

        dfs()
        # for idx, ss in enumerate(arr):

        return self.res

        # a, b, c
        # ''
        # 