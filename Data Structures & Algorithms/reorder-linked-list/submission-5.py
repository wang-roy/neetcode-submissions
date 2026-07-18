# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # while fast.next and fast.next.next:
        #     fast = fast.next.next
        #     slow = slow.next
        
        
        curr = slow.next
        prev = None
        slow.next = None
        ## reverse
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        ## merge reversed second half and first half
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2