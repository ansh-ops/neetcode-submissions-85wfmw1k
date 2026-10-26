class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_count = {0: 1}
        count = 0
        current_sum = 0

        for num in nums:
            current_sum += num
            count += prefix_count.get(current_sum - k, 0)
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return count

        