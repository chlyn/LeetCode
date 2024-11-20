# Problem: 0009 - Palindrom Number
# Source: https://leetcode.com/problems/palindrome-number/description/
# Date: 11-19-2024

class Solution:
    def isPalindrome(self, x: int) -> bool:

        num = list(str(x))
        num_reverse = num.copy()
        num_reverse.reverse()

        if num == num_reverse:
            return True
        else:
            return False
                