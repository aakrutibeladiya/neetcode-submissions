# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:    
        res = 0
   
        def dfs(root):
            nonlocal res
        
            if not root: # base case
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res, left+right) # take the left and right longest path avialable and compare with last max res 

            return 1+ max(left,right) # pass longest path for parent with its subtree

        dfs(root)
        return res

    
    