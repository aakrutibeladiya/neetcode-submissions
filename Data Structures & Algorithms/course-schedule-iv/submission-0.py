class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = [] # boolean values for queries
        prereqmap = [set() for _ in range(numCourses)] # for each node we have list of prereqs
        adjmap = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            adjmap[course].append(pre)
            indegree[pre] += 1

        que = deque(i for i in range(numCourses) if indegree[i] == 0)

        while que:
            course = que.popleft()
            for adj in adjmap[course]:
                prereqmap[adj].add(course)
                prereqmap[adj] |= prereqmap[course]    
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    que.append(adj)

        
        return [u in prereqmap[v] for u, v in queries]




