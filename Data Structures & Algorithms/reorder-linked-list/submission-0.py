# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        middle = slow
        while middle:
            middle.next ,prev ,middle = prev ,middle ,middle.next
        
        first = head
        second = prev

        while second.next:
            first.next ,first = second ,first.next
            second.next ,second = first ,second.next
