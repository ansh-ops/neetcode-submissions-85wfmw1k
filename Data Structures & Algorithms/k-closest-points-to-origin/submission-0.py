class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        
        for i,j in points:
            distance = (i**2 + j**2)
            dist.append([distance,i,j])
        
        heapq.heapify(dist)
        res = []
        while k > 0:
            distance, x, y = heapq.heappop(dist)
            res.append([x,y])
            k -= 1
        
        return res
    