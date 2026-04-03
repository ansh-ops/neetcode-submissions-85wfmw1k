class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = [1]*len(nums)
        setnums = list(set(nums))
        for i in range(len(setnums)):
            for j in range(1, len(setnums)):
                if setnums[i]+j not in setnums:
                    break
                if setnums[i]+j in setnums:
                    longest[i] += 1
                
        
        if not nums:
            return 0
        else:
            return max(longest)