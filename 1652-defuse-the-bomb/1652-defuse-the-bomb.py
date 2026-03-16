class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        left = 0
        arr_sum = 0
        for c in range(abs(k)):
            arr_sum += code[c]
        
        for right in range(abs(k), n+abs(k)):
            if k < 0:
                res[right % n] = arr_sum
            if k > 0:
                res[left - 1 % n] = arr_sum
            arr_sum += code[right % n] - code[left]
            left += 1
        return res
        # for i in range(n):
        #     if k > 0:
        #         for j in range(i+1, i+1+k):
        #             res[i] += code[j % n]
        #     if k < 0:
        #         for j in range(i+k, i):
        #             res[i] += code[j % n] 
        
        # return res
