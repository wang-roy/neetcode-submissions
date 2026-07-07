# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = [(root, None)]
        good_count = 0
        while (len(queue) > 0):
            node, path_max = queue.pop(0)
            if node is None:
                continue
            print(f"node: {node.val}")
            print(f"path max: {path_max}")
            
            if path_max == None or node.val >= path_max:
                path_max = node.val
                good_count += 1
            queue.append((node.left, path_max))
            queue.append((node.right, path_max))
        
        return good_count


        