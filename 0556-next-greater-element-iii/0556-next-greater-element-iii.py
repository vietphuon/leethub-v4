class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = []
        m = n
        while n:
            digits.append(n % 10)
            n = n // 10
        
        r = len(digits) # n = 123 -> digits = [3, 2, 1]
        # print(digits)
        for i in range(r-1):
            if digits[i] > digits[i+1]:
                print("Detect:", digits, "i:", i)
                # perform swap -> naive swap won't work
                # digits[i], digits[i+1] = digits[i+1], digits[i]
                # print("First swap:", digits)

                # find the smallest right-most j to swap w/ i+1
                j_min = i # orginally digits[i+1]
                for j in range(i+1):
                    if digits[j] > digits[i+1] and digits[j] < digits[j_min]:
                        # digits[j], digits[i] = digits[i], digits[j] not just swap any j sastify
                        j_min = j
                
                # digits[j_min] = digit_min
                digits[j_min], digits[i+1] = digits[i+1], digits[j_min]
                print("Second swap:", digits, "j_min:", j_min)

                # Step 2: now sort digits[0..i] to be in ??? order
                digits[:i+1] = sorted(digits[:i+1], reverse=True)
                break

        # digits.sort(key=lambda x: -x)
        digits.reverse()

        new_n = 0
        for d in digits:
            new_n = new_n * 10 + d
        
        if new_n == m or new_n > 2**31 - 1 or new_n < -2**31:
            return -1
        else:
            return new_n