class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:
            return 0
        hs = {i: [] for i in range(n)}
        res = 0
        for i, j in roads:
            hs[i].append(j)
            hs[j].append(i)
        arr = [i for i in range(n)]
        arr.sort(key=lambda x: -len(hs[x]))
        for j in range(n-1):
            for i in range(j+1, n):
                res = max(res, len(hs[arr[j]]) + len(hs[arr[i]]) - 1 if arr[j] in hs[arr[i]] else len(hs[arr[j]]) + len(hs[arr[i]]))
        return res