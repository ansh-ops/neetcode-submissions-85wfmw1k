class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = [[] for i in range(numCourses)]
        indegree = [0] * numCourses
        for i,j in prerequisites:
            indegree[j] += 1
            adjlist[i].append(j)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        finish = 0
        res = []
        
        while q:
            node = q.popleft()
            res.append(node)
            finish += 1

            for nei in adjlist[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if finish != numCourses:
            return []
        
        return res[::-1]

            
            

        