class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = nums.count(val)

        i = 1
        while i <= k:
            nums.remove(val)
            i += 1

        return len(nums)