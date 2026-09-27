class MyStack:

    def __init__(self):
        self.queue = []
        self.temp = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        
    def pop(self) -> int:
        for i in range(len(self.queue) - 1):
            self.temp.append(self.queue.pop(0))
        
        temp = self.queue.pop(0)
        self.queue = self.temp
        self.temp = []
        return temp


    def top(self) -> int:
        temp = self.pop()
        self.push(temp)
        return temp
        

    def empty(self) -> bool:
        return not len(self.queue)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()