class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        left, right = intervals[0]
        res = []
        for i, j in intervals:
            if right >= i:
                right = max(right, j) # new interval [left, j]
            else:
                res.append([left, right])
                left = i
                right = j
        
        res.append([left, right])
        return res