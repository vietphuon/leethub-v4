class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ms = 0
        hs = {}
        left = 0
        for idx, char in enumerate(s): # char is right poitner
            if char not in hs: 
                hs[char] = idx
            else:
                # char in hs
                if hs[char] >= left:
                    left = hs[char] + 1 # left pointer move forward duplicated char 1
                
                hs[char] = idx # update newest idx of duplicated char 2

            if ms < idx - left + 1:
                ms = idx - left + 1

        return ms
            