class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
            adj = [[] for _ in range(n+1)]

            for u,v,w in times:
                adj[u].append((v,w))

            heap = [(0,k)]
            heapq.heapify(heap)

            max_time = 0
            visited = set()
            while heap:
                time_so_far, node = heapq.heappop(heap)
                
                if node in visited:
                    continue
                visited.add(node)

                max_time = max(max_time, time_so_far)

                for neighbor, time in adj[node]:
                    heapq.heappush(heap, (time + time_so_far,neighbor))
            return max_time if len(visited) == n else -1