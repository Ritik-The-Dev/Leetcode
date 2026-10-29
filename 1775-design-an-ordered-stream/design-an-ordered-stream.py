class OrderedStream:

    def __init__(self, n: int):
        self.curr = 0
        self.result = [""] * n

    def insert(self, idKey: int, value: str) -> list[str]:
        
        self.result[idKey - 1] = value

        start = self.curr

        while self.curr < len(self.result) and self.result[self.curr]:
            self.curr += 1

        return self.result[start : self.curr]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)