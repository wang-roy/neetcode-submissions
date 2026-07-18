# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode], prev: Optional[ListNode]=None) -> Optional[ListNode]:
        if not head:
            return prev

        tmp = head.next
        head.next = prev

        return self.reverseList(tmp, head)

        # 0 -> 1 -> 2 -> None
        # recursive(0)
        # None <- 0 1 -> 2 -> None
        # recursive(1, 0)
        # None <- 0 <- 1    2
        # recursive(2, 1)
        # 0 <- 1 <- 2
        # recursive(None, 2)
    