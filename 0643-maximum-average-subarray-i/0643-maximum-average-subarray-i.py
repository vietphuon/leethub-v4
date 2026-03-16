class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        hs = {}
        left = 0
        res = 0
        acc = 0
        for right, num in enumerate(nums): # [0..5]
            if right < k:
                res += num
                acc = res
            else:
                res += nums[right] - nums[left]
                acc = max(acc, res)
                left += 1
        return acc / k