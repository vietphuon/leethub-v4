class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0
        b_count = 0
        
        for ch in s:
            if ch == 'b':
                b_count += 1
            else:  # ch == 'a'
                if b_count > 0:
                    # conflict! greedily delete the cheaper option
                    deletions += 1
                    b_count -= 1   # why decrement here?
        
        return deletions