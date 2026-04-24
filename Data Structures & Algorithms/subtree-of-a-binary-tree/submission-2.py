# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(p,q):
    if p == None and q == None:
        return True

    if p and q and p.val == q.val:   
        return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

    return False

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False

        if not subRoot:
            return True

        if isSameTree(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)