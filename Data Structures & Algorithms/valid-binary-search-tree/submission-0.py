# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isvalid(node,mini,maxi):
    if not node:
        return True
    
    if node.val <= mini or node.val >= maxi:
        return False

    return isvalid(node.left,mini,node.val) and isvalid(node.right,node.val,maxi)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return isvalid(root,float('-inf'),float('inf'))