class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        visiting = set()

        def dfs(i):
            if i in visiting:
                return False
            
            if adjList[i] == []:
                return True
            
            visiting.add(i)

            for pre in adjList[i]:
                if not dfs(pre):
                    return False
            visiting.remove(i)
            adjList[i] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
            


        