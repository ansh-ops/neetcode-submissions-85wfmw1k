class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for cr,pr in prerequisites:
            preMap[cr].append(pr)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True
            
            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for cr in range(numCourses):
            if not dfs(cr): return False
        
        return True



        