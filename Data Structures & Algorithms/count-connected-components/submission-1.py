class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()

        def dfs(i):
            visited.add(i)
            for neighbour in adj[i]:
                if neighbour not in visited:
                    dfs(neighbour)
        
        components = 0
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
        
        return components
                
            


        