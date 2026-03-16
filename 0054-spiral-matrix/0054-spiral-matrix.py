class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        maxtrix_len = m*n
        res = []
        left, right = 0, 0
        lower_n, lower_m = 0, 1
        res.append(matrix[0][0])
        while True:
            while right < n - 1:
                right += 1
                res.append(matrix[left][right])
                if len(res) == maxtrix_len:
                    return res
            
            while left < m - 1:
                left += 1
                res.append(matrix[left][right])
                if len(res) == maxtrix_len:
                    return res
            
            while right > lower_n:
                right -= 1
                res.append(matrix[left][right])
                if len(res) == maxtrix_len:
                    return res
            
            while left > lower_m:
                left -= 1
                res.append(matrix[left][right])
                if len(res) == maxtrix_len:
                    return res
            
            if len(res) == maxtrix_len:
                    return res
            
            n -= 1
            m -= 1
            lower_n += 1
            lower_m += 1

        return res