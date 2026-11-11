class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = [[x**2 + y**2, x, y] for x,y in points]
        output = []
        heapq.heapify(dis)

        while k > 0:
            dist, x, y = heapq.heappop(dis)
            output.append([x,y])
            k -= 1
        return output




        