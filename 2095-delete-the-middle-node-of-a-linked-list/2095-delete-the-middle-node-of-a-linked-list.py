class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = fast = temp = head

        if head.next is None:
            return head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        while temp.next != slow:
            temp = temp.next
            
        temp.next = slow.next
        return head