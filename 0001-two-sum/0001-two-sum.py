class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hs = {}
        for i in range(n):
            if nums[i] not in hs:
                hs[target - nums[i]] = i
            else:
                return [i, hs[nums[i]]]