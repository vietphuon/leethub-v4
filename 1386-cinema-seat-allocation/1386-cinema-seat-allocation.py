class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        def checkRow(seat: List[int]):
            if seat[1]*seat[2]*seat[3]*seat[4] and seat[5]*seat[6]*seat[7]*seat[8]:
                return 2
            if seat[1]*seat[2]*seat[3]*seat[4] or seat[5]*seat[6]*seat[7]*seat[8] or seat[3]*seat[4]*seat[5]*seat[6]:
                return 1
            return 0
        hs = {}
        # seats = [[1]*10 for i in range(n)]
        for r, c in reservedSeats:
            # print(r, c)
            # seats[r-1][c-1] = 0 -> n ~ 10**9 memory limit
            if r-1 not in hs:
                hs[r-1] = [1]*10
            hs[r-1][c-1] = 0 
        
        print(hs)
        conflicts = len(hs) # number of rows need handle
        res = (n - conflicts)*2

        for seat in hs:
            print("Seat:", seat)
            res += checkRow(hs[seat])
        
        return res