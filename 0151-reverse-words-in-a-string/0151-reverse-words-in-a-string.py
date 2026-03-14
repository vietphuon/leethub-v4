class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() + ' '
        arr = []
        curr = ''
        for c in s:
            print(c, curr, arr)
            if c != ' ':
                curr += c
            elif curr:
                arr = [curr] + arr
                curr = ''
            else:
                continue
        
        return ' '.join(arr)