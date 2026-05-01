# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def nodes(root):
    if not root:
        return []
    
    l = []
    l.append(root.val)
    l+=nodes(root.left)
    l+=nodes(root.right)

    return l

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = nodes(root)
        lst.sort()
        return lst[k-1]