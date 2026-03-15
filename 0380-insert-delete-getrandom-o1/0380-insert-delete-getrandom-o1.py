import random

class RandomizedSet:

    def __init__(self):
        self.arr = [] # idx -> val
        self.hs = {} # val -> idx

    def insert(self, val: int) -> bool:
        # print(self.arr, ' ', self.hs)
        if val not in self.hs:
            self.arr.append(val)
            idx = len(self.arr) - 1
            self.hs[val] = idx
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        # print(self.arr, ' ', self.hs)
        if val in self.hs:
            # Get idx from hash
            idx = self.hs[val]
            # Remove from list
            # Option 1: self.arr = self.arr[:idx] + self.arr[idx+1:] (!) leaved a hole in list
            # Option 2: swap idx with -1
            self.hs[self.arr[-1]] = idx
            self.hs.pop(self.arr[idx])
            self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
            self.arr.pop(-1)
            return True
        else:
            return False

    def getRandom(self) -> int:
        # print(self.arr, ' ', self.hs)
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()