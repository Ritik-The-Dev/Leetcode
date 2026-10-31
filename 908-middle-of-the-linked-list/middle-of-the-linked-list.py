# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        
        n = 0

        pointer = head

        while pointer :
            pointer = pointer.next
            n += 1

        pointer = head
        i = 0

        while i < n // 2:
            pointer = pointer.next
            i += 1

        return pointer