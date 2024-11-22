# Problem: 0001 - Two Sum
# Source: https://leetcode.com/problems/two-sum/description/
# Date: 11-16-2024

########################################################################################################## 
#  
#  UNDERSTANDING
#    
#  We are given a list of numbers that eventually sum up to the given target number. To find the index of 
#  the pair,  we can iterate through each number and add it to the other numbers until the target it found.
#   
#  BRUTE FORCE APPROACH
#   
#  1) Create a for loop to iterate through each number in the list.
#  2) Create another for loop within the same for loop to iterate through the other numbers in the list.
#  3) Create an if-statement to check if the current element 'i' and the other pair 'j' sums up to the 
#     target.
#  4) If the pairs are found, return the index.
#
#########################################################################################################

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range (n - 1):
            for j in range (i + 1, n):
                    if nums[i] + nums[j] == target:
                        return [i, j]