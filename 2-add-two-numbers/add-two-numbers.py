# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
        carryover = 0

        newList = ListNode(0)
        current = newList

        while l1 or l2 or carryover:
            total = carryover

            if l1:
                total += l1.val
                l1 = l1.next
            if l2 :
                total += l2.val
                l2 = l2.next

            carryover = total // 10
            digit = total % 10
        
            current.next = ListNode(digit )
            current = current.next

            
        return newList.next