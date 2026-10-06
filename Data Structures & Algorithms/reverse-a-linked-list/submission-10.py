# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        p2 = head
        if curr and curr.next:
            curr = curr.next
            while curr:
                temp = curr.next
                curr.next = p2
                p2 = curr
                curr = temp
            head.next = None
            return p2
        else:
            return curr