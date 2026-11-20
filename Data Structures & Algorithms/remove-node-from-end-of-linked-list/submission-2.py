class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        l = dummy
        r = head
        
        while n > 0 and r:
            r = r.next
            n -= 1
        
        while r:
            l = l.next
            r = r.next
            
        l.next = l.next.next
        return dummy.next