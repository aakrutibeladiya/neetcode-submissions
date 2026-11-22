class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] # index monotonic 
        res = 0


        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                mid = height[stack.pop()]
                if stack:
                    dis = i - stack[-1]-1
                    left = height[stack[-1]]
                    right = height[i]
                    h = min(left,right) - mid
                    res += h*dis 
            stack.append(i)
        return res

