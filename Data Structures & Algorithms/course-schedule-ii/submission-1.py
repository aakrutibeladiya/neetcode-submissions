class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = [] 
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            adj[course].append(prereq)
            indegree[prereq] += 1
        
        que = deque([i for i in range(numCourses) if indegree[i] == 0])

        completeCounter = 0
        while que:
            course = que.popleft()
            res.append(course)
            completeCounter += 1
            for pre in adj[course]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    que.append(pre)
            

        if completeCounter != numCourses:
            return []
        return res[::-1]       




    

