# Problem: 0027 - Remove Element
# Source: https://leetcode.com/problems/remove-element/description/
# Date: 11-21-2024

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = nums.count(val)

        i = 1
        while i <= k:
            nums.remove(val)
            i += 1

        return len(nums)