# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        if list1 and list2:
            head = list1 if min(list1.val, list2.val) == p1.val else list2
        elif list1:
            head = list1
        else:
            head = list2
        
    
            
        while p1 and p2:
            adj1 = p1.next
            adj2 = p2.next
            if p1.val <=  p2.val:
                if adj1 and adj1.val <= p2.val:
                    p1 = adj1
                    continue
                else:
                    p1.next = p2
                    p1 = adj1

            else:
                if adj2 and adj2.val < p1.val:
                    p2 = adj2
                    continue
                else:
                    p2.next = p1
                    p2 = adj2


        return head

