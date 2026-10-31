class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)

    def get(self, index: int) -> int:
        i = 0
        head = self.head.next
        while head and i < index:
            head = head.next
            i += 1
        if head :
            return head.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val , self.head.next)
        self.head.next = newNode

    def addAtTail(self, val: int) -> None:
        head = self.head
        while head.next:
            head = head.next
        head.next = ListNode(val ,None)

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        prev = self.head
        
        while prev and i < index:
            prev = prev.next
            i += 1

        prev.next = ListNode(val , prev.next)


    def deleteAtIndex(self, index: int) -> None:
        i = 0
        
        head = self.head
        
        while head and i < index:
            head = head.next
            i += 1

        if head.next:
            head.next = head.next.next        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)