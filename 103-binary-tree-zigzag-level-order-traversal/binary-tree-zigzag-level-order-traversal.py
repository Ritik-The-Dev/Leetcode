# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        
        if not root:
            return []
            
        from collections import deque
        queue = deque([root])

        result = []
        i = 0

        while queue:
            
            curr = []

            for _ in range(len(queue)):
                node = queue.popleft()
                curr.append(node.val)
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if i % 2 != 0:
                curr.reverse()

            result.append(curr)
            i += 1

        return result