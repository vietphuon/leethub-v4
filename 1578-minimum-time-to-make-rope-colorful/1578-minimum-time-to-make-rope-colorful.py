class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        stack = []  # stack of (color, cost) that we've "kept"

        for idx in range(len(colors)):
            if idx and colors[idx] == stack[-1][0]:
                # if top of stack has same color as current...
                # who should we remove?
                if neededTime[idx] < stack[-1][1]:
                    total += neededTime[idx]
                else:
                    total += stack[-1][1]
                    stack.pop(-1)
                    stack.append([colors[idx], neededTime[idx]])
            else:
                stack.append([colors[idx], neededTime[idx]])
        
        return total
    
    def minCost1(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) == 1:
            return 0
        
        hs = {}

        for idx in range(len(neededTime)):
            if idx and colors[idx] == colors[idx-1]:
                oidx = idx-1
                if neededTime[idx] < neededTime[oidx]:
                    return neededTime[idx] + self.minCost(
                        colors=colors[:idx] + colors[idx+1:], 
                        neededTime=neededTime[:idx] + neededTime[idx+1:]
                    )
                else:
                    return neededTime[oidx] + self.minCost(
                        colors=colors[:oidx] + colors[oidx+1:], 
                        neededTime=neededTime[:oidx] + neededTime[oidx+1:]
                    )
            else:
                pass
        
        return 0
        