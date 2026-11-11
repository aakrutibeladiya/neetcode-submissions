class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        largestOrdStones = [-x for x in stones]
        heapq.heapify(largestOrdStones)
        while len(largestOrdStones) > 1:
            x , y = -heapq.heappop(largestOrdStones),                    -heapq.heappop(largestOrdStones)
            if not x == y:
                newVal = abs(x-y)
                heapq.heappush(largestOrdStones, -newVal)
        return abs(largestOrdStones[0]) if largestOrdStones else 0
