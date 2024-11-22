// Problem: 0001 - Two Sum
// Source: https://leetcode.com/problems/two-sum/description/
// Date: 11-16-2024

/*******************************************************************************************************
 *  
 *  UNDERSTANDING
 *     
 *  We are given a list of numbers that eventually sum up to the given target number. To find the index 
 *  of the pair, we can iterate through each number and add it to the other numbers until the target it 
 *  found.
 *   
 *  BRUTE FORCE APPROACH
 *   
 *  1) Initialize an array in as size of 2 with the values of 0. (This will be used to store the result)
 *  1) Create a for loop to iterate through each number in the list.
 *  2) Create another for loop within the same for loop to iterate through the other numbers in the list.
 *  3) Create an if-statement to check if the current element 'i' and the other pair 'j' sums up to the 
 *     target.
 *  4) If the pairs are found, update the elements in the result with the index of the pair.
 *  
*******************************************************************************************************/


class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int n = nums.length;
        int[] result = new int[2];

        for(int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if ((nums[i] + nums[j]) == target)
                {
                    result[0] = i;
                    result[1] = j;
                }
            }
        }

        return result;
    }
}