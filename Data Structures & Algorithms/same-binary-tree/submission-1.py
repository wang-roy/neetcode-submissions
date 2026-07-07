# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(p, q):
            p_queue = [p]
            q_queue = [q]
            while len(p_queue) > 0 and len(q_queue) > 0: 
                p_node = p_queue.pop(0)
                q_node = q_queue.pop(0)
                if p_node and q_node and p_node.val != q_node.val:
                    return False
                elif p_node and not q_node:
                    return False
                elif not p_node and q_node:
                    return False
                elif not p_node and not q_node: # both null
                    continue
                p_queue.append(p_node.left)
                p_queue.append(p_node.right)

                q_queue.append(q_node.left)
                q_queue.append(q_node.right)
            
            return len(p_queue) == len(q_queue)
        return bfs(p, q)
