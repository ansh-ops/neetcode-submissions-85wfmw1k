class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum, maxsub = 0, nums[0]

        for i in nums:
            if currsum < 0:
                currsum = 0
            
            currsum += i
            maxsub = max(maxsub, currsum)

        return maxsub