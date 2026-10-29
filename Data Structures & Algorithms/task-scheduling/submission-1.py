class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for i in tasks:
            count[i] = 1 + count.get(i, 0)
        
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                task = 1 + heapq.heappop(maxHeap)
                if task:
                    q.append([task, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time

        