class ListNode():
    def __init__(self, val: int, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
        
class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def append(self, value: int) -> None:
        self.tail.next = ListNode(value, self.tail)
        self.tail = self.tail.next

    def appendleft(self, value: int) -> None:
        newNode = ListNode(value, self.head, self.head.next)
        if not self.tail == self.head:
            self.head.next.prev = newNode
        else:
            self.tail = newNode
        self.head.next = newNode
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        temp = self.tail.val
        self.tail.prev.next = None
        self.tail = self.tail.prev
        return temp

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        temp = self.head.next.val
        if self.head.next == self.tail:
            self.tail = self.tail.prev
        self.head.next = self.head.next.next
        if self.head.next:
            self.head.next.prev = self.head
        return temp
        
