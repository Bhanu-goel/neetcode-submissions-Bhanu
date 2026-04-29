# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(root,maxnode):
    if not root:
        return 0
    
    count = 0
     
    if root.val >= maxnode:
        count = 1
    
    maxnode = max(maxnode,root.val)

    count += dfs(root.left,maxnode)
    count += dfs(root.right,maxnode)

    return count

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return dfs(root,root.val)