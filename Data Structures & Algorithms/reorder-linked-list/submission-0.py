# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast and slow pointer mode

        def reverse(head):
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

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None   # break the list
        otherHead = reverse(second)

        curr1 = head
        curr2 = otherHead
        while curr1 and curr2:
            next1 = curr1.next
            next2 = curr2.next
            curr1.next = curr2
            curr2.next = next1
            curr1 = next1
            curr2 = next2

        


        