# Problem: 0001 - Two Sum
# Source: https://leetcode.com/problems/two-sum/description/
# Date: 11-16-2024

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range (n - 1):
            for j in range (i + 1, n):
                    if nums[i] + nums[j] == target:
                        return [i, j]