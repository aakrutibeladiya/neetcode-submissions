class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgemap = defaultdict(list)
        for i,j in edges:
                edgemap[i].append(j)
                edgemap[j].append(i)
        res = 0
        visited = set()
        def dfs(node):
            for nei in edgemap[node]: 
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
                

            
        for node in range(n):
            if node not in visited :
                visited.add(node)
                dfs(node)
                res += 1
        
        return res 

        