class Solution:
    def jump(self, nums: List[int]) -> int:
        final = len(nums) - 1
        jump = 0
        l = r = 0

        while r < final:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            jump += 1
        
        return jump


        