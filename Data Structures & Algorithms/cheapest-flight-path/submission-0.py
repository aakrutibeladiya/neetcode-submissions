class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = collections.defaultdict(list)
        for st,en,co in flights:
            adj[st].append((en,co))

        mincost = [float("inf")] * n
        dq = deque([(0,src,0)])
        mincost[src] = 0
        # stops = k 
        print(mincost)
        while dq:
            cost,node,stops = dq.popleft()
            if stops > k:
                continue
            for nei, w in adj[node]:
                nextcost = cost + w
                if nextcost < mincost[nei]:
                    mincost[nei] = nextcost
                    dq.append((nextcost,nei,stops+1))
                
        return mincost[dst] if mincost[dst] != float("inf") else -1
            

