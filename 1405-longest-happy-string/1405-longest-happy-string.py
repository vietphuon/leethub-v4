class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        counts = [(a, 'a'), (b, 'b'), (c, 'c')]  # store (count, char) for a, b, c
        
        while True:
            counts.sort(key=lambda x: x[0], reverse=True)
            print(counts)
            # Determine which character to use
            char = counts[0][1]
            char_idx = 0
            # Check if top choice would cause "aaa" (look at last 2 chars of res)
            if len(res) > 1:
                if char != res[-1] or char != res[-2]:
                    pass
                # If so, try second choice
                elif counts[1][1] != res[-1] or counts[1][1] != res[-2]:
                    char_idx = 1
                    char = counts[1][1]
                # If neither works, break
                else:
                    break
            
            if not counts[char_idx][0]:
                break
            chosen_char = char
            res.append(chosen_char)
            # decrement chosen count
            counts[char_idx] = (counts[char_idx][0] - 1, counts[char_idx][1])
        
        return "".join(res)