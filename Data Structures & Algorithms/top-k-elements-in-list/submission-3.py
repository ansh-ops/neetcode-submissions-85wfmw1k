class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            countmap[i] = 1 + countmap.get(i, 0)

        for num, cnt in countmap.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        