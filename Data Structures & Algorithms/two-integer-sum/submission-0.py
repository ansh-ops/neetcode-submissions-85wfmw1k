class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = [] 
        for i in range(len(nums)):
            for n in range(i+1,len(nums)):
                if nums[i] + nums[n] == target:
                    answer.append(i)
                    answer.append(n)
        return answer

