class Solution:
    def decodeString(self, s: str) -> str:
        stack = []       # stores (current_string, current_k) at each '['
        cur_str, cur_k = "", 0

        for ch in s:
            if ch.isdigit():
                cur_k = cur_k * 10 + int(ch)  # why *10?
            elif ch == '[':
                # save context, reset
                stack.append((cur_str, cur_k))
                cur_str, cur_k = "", 0
            elif ch == ']':
                # restore context
                prev_str, k = stack.pop()
                cur_str = prev_str + cur_str * k # combine prev_str and repeated cur_str
            else:
                cur_str += ch

        return cur_str