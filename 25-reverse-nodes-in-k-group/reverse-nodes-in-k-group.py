# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        
        totalLen = 0

        start = head

        while start:
            start = start.next
            totalLen += 1

        start = head

        newHead = None
        prevTail = None

        while start and totalLen >= k:

            curr = start

            i = 0

            while i < k:
                start = start.next
                i += 1

            prev = start
            currTail = curr

            i = 0

            while i < k:
                temp = curr.next
                curr.next = prev 
                prev = curr
                curr = temp
                i += 1

            if not newHead:
                newHead = prev

            if prevTail:
                prevTail.next = prev

            prevTail = currTail

            totalLen -= k

        return newHead    

