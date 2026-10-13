# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        
        def check(root1 , root2):
            if not root1 or not root2:
                return root1 == root2
            
            if root1.val != root2.val:
                return False

            res1 = check(root1.left , root2.right)
            res2 = check(root1.right , root2.left)

            return res1 and res2

        return check(root,root)
