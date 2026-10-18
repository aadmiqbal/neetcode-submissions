class MinStack:

    def __init__(self):
        self.data = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.mins:
            self.mins.append(val)
        else:
            if val <= self.mins[-1]:
                self.mins.append(val)
        self.data.append(val)

    def pop(self) -> None:
        if self.data[-1] == self.mins[-1]:
            self.mins.pop()
        self.data.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        if self.data:
            return self.mins[-1]
        
