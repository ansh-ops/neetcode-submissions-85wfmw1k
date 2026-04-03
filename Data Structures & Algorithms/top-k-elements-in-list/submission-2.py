class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = {}
        for i in range(len(nums)):
            countmap[nums[i]] = 1 + countmap.get(nums[i],0)
        
        sort_map = {k:v for k,v in sorted(countmap.items(), key=lambda u:u[1],reverse =True)}
        final = list(sort_map.keys())
        return final[:k]
