class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hs = {}
        left = 0
        res = 0
        for idx, right in enumerate(nums):
            if right not in hs:
                hs[right] = 1
            else:
                hs[right] += 1

        for idx, right in enumerate(nums):
            if right + 1 in hs:
                res = max(res, hs[right] + hs[right + 1])
    
        return res