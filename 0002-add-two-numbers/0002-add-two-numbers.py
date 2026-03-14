# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        curr = l3
        acc = 0

        while l1 or l2 or acc: 
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            new = (v1 + v2 + acc) % 10
            curr.next = ListNode(new)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            acc = (v1 + v2 + acc - new) // 10

        return l3.next
