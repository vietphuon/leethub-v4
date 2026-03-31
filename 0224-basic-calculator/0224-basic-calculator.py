class Solution:
    def calculate(self, s: str) -> int:
        stack = deque([])
        res = 0
        sign = 1
        num = 0

        # 1 + 2 - (2 - 3)
        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)
            elif ch == '+':
                res += sign * num
                num = 0
                sign = 1
            elif ch == '-':
                res += sign * num
                num = 0
                sign = -1
            elif ch == '(':
                stack.append((res, sign)) # 3, -
                res = 0
                sign = 1
            elif ch == ')':
                res += sign * num # -1
                num = res
                res, sign = stack.pop()
        
        res += sign * num
        return res
    
    def calculate1(self, s: str) -> int:
        stack = []
        res = 0
        sign = 1
        num = 0

        # 1 + 2 - (2 - 3)
        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)
            elif ch == '+':
                res += sign * num
                num = 0
                sign = 1
            elif ch == '-':
                res += sign * num
                num = 0
                sign = -1
            elif ch == '(':
                stack.append(res) # 3
                stack.append(sign) # -
                res = 0
                sign = 1
            elif ch == ')':
                res += sign * num # -1
                num = res
                sign = stack.pop() # -
                res = stack.pop() # 3
        
        res += sign * num
        return res