from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        sorted_c = dict(sorted(c.items(), key = lambda item: item[1]))
        ls = list(sorted_c.keys())
        return ls[-k::1]

        