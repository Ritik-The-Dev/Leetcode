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
        newHead = None
        prevTailGroup = None

        while start and totalLen >= k :
            
            i = 0

            curr = start # 3 -> 4 -> 5

            while i < k:
                start = start.next
                i += 1

            i = 0

            prev = start  # 2 -> 1 -> 3
            groupTail = curr

            while curr and i < k:
                temp = curr.next # 3
                curr.next = prev 
                prev = curr
                curr = temp
                i += 1
            
            if not newHead:
                newHead = prev
            
            if prevTailGroup:
                prevTailGroup.next = prev

            prevTailGroup = groupTail
            totalLen -= k

        return newHead if newHead else Head