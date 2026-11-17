from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False

        edgemap = defaultdict(list)
        for i,j in edges:
                edgemap[i].append(j)
                edgemap[j].append(i)

        visit = set()
        que = deque([(0,-1)])
        visit.add(0)
        while que:
            node,par = que.popleft()
            for nei in edgemap[node]:
                if nei == par:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                que.append((nei,node))


        # print("edgemap",edgemap)
        return len(visit) == n
