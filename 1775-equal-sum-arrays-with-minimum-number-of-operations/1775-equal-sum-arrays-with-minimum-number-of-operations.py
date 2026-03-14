class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        if sum1 > sum2:
            nums1, nums2 = nums2, nums1
        
        # nums1 always samller sum
        gap = abs(sum2 - sum1)

        gain = [6 - x for x in nums1] + [x - 1 for x in nums2]
        gain.sort(key=lambda x: -x)

        # max gain can't close gap
        if sum(gain) < gap:
            return -1
        
        ops, idx = 0, 0
        while gap > 0:
            gap -= gain[idx]
            ops += 1
            idx += 1
        
        return ops
        
