# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        que = deque([root])
        res = []
    
        while que:
            clevelnodes= []
            for _ in range(len(que)):
                node = que.popleft()
                if node:
                    clevelnodes.append(node.val)
                    if node.left or node.right:
                        que.append(node.left)
                        que.append(node.right)
                
            res.append(clevelnodes[-1])
        return res
        

