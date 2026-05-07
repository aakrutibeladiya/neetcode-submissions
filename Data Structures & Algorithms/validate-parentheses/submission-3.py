class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openCloseDic = {")" :"(","}":"{","]":"["}
        for i in s:
            if i in openCloseDic:
                if stack and stack[-1] == openCloseDic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False