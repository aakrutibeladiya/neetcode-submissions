class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # [temp,index]
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and stack[-1][0] < temp:
                lastItem = stack.pop()
                res[lastItem[1]] = i - lastItem[1]
            stack.append([temp,i])

        return res        