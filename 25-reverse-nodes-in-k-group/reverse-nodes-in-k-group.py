# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        
        if k <= 1 or not head:
            return head

        # Calculate The length Of The LinkedList
        totalLen = 0
        start = head

        while start :
            start = start.next
            totalLen += 1
        
        # Reverse and Apppend
        start = head
        
        newHead = None # 2 -> 1 -> 3 -> 4 -> 5
        prevTailGroup = None 

        while start and totalLen >= k :
            
            i = 0

            curr = start # 3

            while i < k:
                start = start.next
                i += 1

            i = 0

            prev = start  # 4 -> 3 -> 5
            groupTail = curr # 3

            while curr and i < k:
                temp = curr.next # 5
                curr.next = prev # 4 -> 3 -> 5
                prev = curr
                curr = temp #4
                i += 1
            
            if not newHead:
                newHead = prev
            
            if prevTailGroup:
                prevTailGroup.next = prev

            prevTailGroup = groupTail
            totalLen -= k

        return newHead if newHead else Head