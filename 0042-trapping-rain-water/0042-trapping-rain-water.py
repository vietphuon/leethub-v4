class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        res = 0

        while left < right:
            if height[left] < height[right]:
                # left side is the bottleneck
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    res += (max_left - height[left])
                left += 1
            else:
                # right side is the bottleneck
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    res += (max_right - height[right])
                right -= 1
        
        return res

    def trap1(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, 0
        res, acc = 0, 0

        while right < n:
            print(res, acc, left, right)
            if height[right] >= height[left]:
                # conclude
                res += acc
                acc = 0
                left = right
            else:
                acc += (height[left] - height[right])
            right += 1
        
        return res