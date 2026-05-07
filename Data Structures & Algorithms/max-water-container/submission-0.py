class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxCapacity = 0

        for i, a in enumerate(heights):
            for j, b in reversed(list(enumerate(heights))):
                cap = min(a,b) * (j-i)
                if cap > maxCapacity:
                    maxCapacity = cap
        return maxCapacity


        