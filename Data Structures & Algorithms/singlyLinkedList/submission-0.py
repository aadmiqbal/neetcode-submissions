class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head
        i = index
        try:
            while i > 0:
                curr = curr.next
                i -= 1
        except Exception as e:
            return -1
        if curr == None:
            return -1
        else:
            return curr.val

    def insertHead(self, val: int) -> None:
        oldHead = self.head
        self.head = ListNode(val)
        self.head.next = oldHead
        if self.tail == None:
            self.tail = self.head

    def insertTail(self, val: int) -> None:
        newtail = ListNode(val)
        if self.tail != None:
            self.tail.next = newtail
    
        self.tail = newtail
        if self.head == None:
            self.head = self.tail
        
    
    def remove(self, index: int) -> bool:
        if self.head == None:
            return False
        if index == 0:
            if self.head == self.tail:
                self.tail = self.head.next
            self.head = self.head.next
            return True
        
        i = 0
        curr = self.head
        try:
            while i < index - 1:
                print("curr: ", curr.val)
                curr = curr.next
                i += 1
            if curr.next == None:
                return False
            if curr.next == self.tail:
                self.tail = curr
            
            curr.next = curr.next.next
            return True
        except Exception as e:
            return False


    def getValues(self) -> List[int]:
        curr = self.head
        arr = []
        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        return arr
        
class ListNode:

    def __init__(self, val: int | None = None):
        self.val = val
        self.next = None
