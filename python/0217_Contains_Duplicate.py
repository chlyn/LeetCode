# Problem: 0217 - Contains Duplicate
# Source: https://leetcode.com/problems/contains-duplicate/description/
# Date: 11-15-2024

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
          
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False