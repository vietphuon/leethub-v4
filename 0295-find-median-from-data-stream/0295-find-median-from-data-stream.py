class MedianFinder:

    def __init__(self):
        self.stack = []

    def addNum(self, num: int) -> None:
        self.stack.append(num)
        self.stack.sort()

    def findMedian(self) -> float:
        # P50
        # print(self.stack)
        return self.findP(50)
    
    def findP(self, n: int = 90) -> float:
        # [10, 20, 30, 40, 50] -> P90 = 46
        left_idx, right_idx = round(len(self.stack) * n / 100) - 1, round(len(self.stack) * n / 100)
        left, right = self.stack[left_idx], self.stack[right_idx] # 3, 4
        # f(4) = 40, f(5) = 50 -> f(4.5) = ? df/dx = (50 - 40) / (5 - 4) = 0.5
        frac_idx = (n / 100) * (len(self.stack) - 1) # 3.6
        frac = left + (frac_idx - left_idx) * (right - left) / (right_idx - left_idx)
        return frac


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()