class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zerocount = 0
        res = [0]*len(nums)
        for n in nums:
            if n == 0:
                zerocount += 1
                continue
            prod *= n

        for i in range(len(nums)):
            if zerocount == 0:
                res[i] += int(prod/nums[i])
            if zerocount == 1:
                indexzero = nums.index(0)
                res[indexzero] = prod

        return res
                

