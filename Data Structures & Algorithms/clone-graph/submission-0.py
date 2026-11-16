"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNewCopy = {}
        #  =>. dfs
        # subproblem => create a copy of the node, create copy of connected node and connect them
        # que: does one node have multiple connected nodes?
        # neighbors => yes

        # => still dfs works
        # base case => 
        # if not node:
        #     return
        # deepcopy = Node(node.val, node.neighbors)
        # for n in node.neighbors:
        #     dfs(n,deepcopy)
        
        
        
        # deepcopy = Null
        def dfs(node):
            if node in oldToNewCopy:
                return oldToNewCopy[node]

            copy = Node(node.val)
            oldToNewCopy[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
            

        return dfs(node) if node else None

