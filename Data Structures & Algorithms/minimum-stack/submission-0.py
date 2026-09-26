class MinStack:

    def __init__(self):
        self.arr = []
        self.top_pointer = -1
        self.mins = []
        

    def push(self, val: int) -> None:
        if not self.arr:
            self.mins.append(val)
        else:
            if val < self.mins[self.top_pointer]:
                self.mins.append(val)
            else:
                self.mins.append(self.mins[self.top_pointer])

        self.arr.append(val)
        self.top_pointer += 1
        

    def pop(self) -> None:
        temp = self.arr.pop()
        self.mins.pop()
        self.top_pointer -= 1
        return temp

    def top(self) -> int:
        return self.arr[self.top_pointer]
        

    def getMin(self) -> int:
        return self.mins[self.top_pointer]

            
