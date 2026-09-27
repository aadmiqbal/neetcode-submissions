class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr != None and i<index:
            curr = curr.next
            i+=1
        if curr == None:
            return -1
        else:
            return curr.val
        

    def insertHead(self, val: int) -> None:
        oldhead = self.head.next
        self.head.next = ListNode(val)
        self.head.next.next = oldhead
        if self.head == self.tail:
            self.tail = self.head.next

        

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        i = 0
        #when removing curr should be one before node to remove
        curr = self.head
        while i < index and curr != None:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        else:
            return False


        

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head.next
        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        return arr
        

class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

