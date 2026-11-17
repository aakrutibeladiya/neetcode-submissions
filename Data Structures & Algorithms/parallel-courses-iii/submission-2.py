class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # n = 4
        # relations = [[1,3],[2,3],[3,4]]
        # time = [2,5,3,4] 
        adj = [[] for _ in range(n)]
        indegree = [0] * n 
        maxTime = time[:]

        for src, dst in relations:
             adj[src-1].append(dst-1)
             indegree[dst-1] += 1   

        que = deque([i for i in range(n) if indegree[i] == 0])

        while que:
            node = que.popleft()

            for nei in adj[node]:
                maxTime[nei] = max(maxTime[nei],maxTime[node] + time[nei])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    que.append(nei)
        
        return max(maxTime)
            
