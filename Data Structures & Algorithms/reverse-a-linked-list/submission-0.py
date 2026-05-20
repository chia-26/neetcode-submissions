# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        prev = head
        curr = prev.next
        nextt = curr.next
        prev.next = None

        while nextt:
            curr.next = prev
            prev = curr
            curr = nextt
            nextt = nextt.next

        curr.next = prev
        
        return curr

        

        
        
