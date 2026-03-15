class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # increase n - 1 but one == decrease one by 1
        nums.sort()
        n = len(nums)
        target = nums[0]
        move = [nums[i] - nums[0] for i in range(n)]
        return sum(move)