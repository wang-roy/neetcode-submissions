# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        firstHalfEnd = math.floor(size/2)
        i = 0
        firstHalf = head
        while i < firstHalfEnd:
            firstHalf = firstHalf.next
            i += 1
            
        curr = firstHalf.next
        prev = None
        firstHalf.next = None
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