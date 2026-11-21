# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:

        if not root :
            return []
                    
        from collections import deque

        queue = deque([root])

        result = []

        i = 0

        while queue:
            curr = []
            
            n = len(queue)
            
            while n :
                node = queue.popleft()

                curr.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                n -= 1
            
            if i % 2 == 1:
                curr.reverse()
            
            result.append(curr)
            i += 1

        return result