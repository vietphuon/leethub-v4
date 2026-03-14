class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            adj[p].append(c)
        
        # 0 = unvisited, 1 = visiting (in current path), 2 = visited (done)
        state = [0] * numCourses
        arr = []
        # print(adj) # [[2], [0], [1]]
        # [0, 0, 0] -> [1, 0, 0] -> [1, 0, 1] -> [1, 1, 1] -> (!) violate
        
        def dfs(course) -> bool:
            # leaf
            if state[course] == 2:
                return True # alr sastify preq
            if state[course] == 1:
                return False # violate cycle

            # visit
            state[course] = 1

            # node
            for nxt in adj[course]:
                if not dfs(nxt):
                    return False
            
            state[course] = 2
            arr.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return arr[::-1]