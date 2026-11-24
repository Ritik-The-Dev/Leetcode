# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        
        if p and q and p.val == q.val:
            sameLeftTree = self.isSameTree(p.left , q.left)
            sameRightTree = self.isSameTree(p.right , q.right)

            return sameLeftTree and sameRightTree

        return True if not p and not q else False