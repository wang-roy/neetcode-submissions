# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[0]
        
    def helper(self, root: Optional[TreeNode], height: Optional[int]=0) -> int:
        if root:
            rightBalanced, rightHeight = self.helper(root.right, height+1)
            leftBalanced, leftHeight = self.helper(root.left, height+1)
            rootHeight = max(rightHeight, leftHeight)
            return (rightBalanced and leftBalanced and abs(rightHeight - leftHeight) <= 1, rootHeight)
        else:
            return True, height

