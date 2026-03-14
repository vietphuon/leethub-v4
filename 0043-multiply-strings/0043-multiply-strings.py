class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        hs = {f"{i}": i for i in range(10)}
        n1, n2 = 0, 0
        for c in num1:
            n1 = n1*10 + hs[c]
        for c in num2:
            n2 = n2*10 + hs[c]
        return str(n1*n2)