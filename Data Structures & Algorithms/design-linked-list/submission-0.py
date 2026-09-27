class ListNode():
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while i < index and curr!=None:
            curr = curr.next
            i+=1
        if curr:
            return curr.val
        else:
            return -1


    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        newNode.prev = self.head
        if self.head.next:
            self.head.next.prev = newNode
        self.head.next = newNode
        if self.head == self.tail:
            self.tail = newNode
        
    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = ListNode(val)
        if index == 0:
            self.addAtHead(val)
            return None
        i = 0
        curr = self.head.next
        while i < index - 1 and curr!=None:
            curr = curr.next
            i+=1
        if curr and curr.next:
            curr.next.prev = newNode
            newNode.next = curr.next
            newNode.prev = curr
            curr.next = newNode
        elif curr and not curr.next:
            self.addAtTail(val)
        else:
            return None
        

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        curr = self.head.next
        while i < index and curr!=None:
            curr = curr.next
            i+=1
        if curr and curr.next:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        elif curr and not curr.next:
            curr.prev.next = None
            self.tail = curr.prev
        else:
            return None

        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)