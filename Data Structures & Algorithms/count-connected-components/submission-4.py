class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        edgemap = defaultdict(list)
        res = 0

        for i,j in edges:
            edgemap[i].append(j)
            edgemap[j].append(i)
        
        def dfs(node):
            for c in edgemap[node]:
                if c not in visited:
                    visited.add(c)
                    dfs(c)

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res += 1
        
        return res

        
        

