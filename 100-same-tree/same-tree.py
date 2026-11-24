# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        
        if not p or not q:
            return not p and not q

        if p.val != q.val:
            return False
        
        result1 = self.isSameTree(p.left , q.left)
        result2 = self.isSameTree(p.right , q.right)

        return result1 and result2