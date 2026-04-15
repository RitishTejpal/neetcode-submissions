# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = []
        q.append(root)
        traversal = []

        while q:
            level = []
            count = len(q)
            for _ in range(count):
                node = q.pop(0)
                if node.left != None: q.append(node.left)
                if node.right != None: q.append(node.right)
                level.append(node.val)
            traversal.append(level)
        
        return traversal

