class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        hs = {}
        for right, num in enumerate(nums):
            if num not in hs:
                hs[num] = right
            else:
                if abs(hs[num] - right) <= k:
                    return True
                
                hs[num] = right
        
        return False