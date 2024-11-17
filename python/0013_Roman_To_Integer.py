# Problem: 0013 - Roman To Integers
# Source: https://leetcode.com/problems/roman-to-integer/description/
# Date: 11-16-2024

class Solution:
    def romanToInt(self, s: str) -> int:

        result = 0

        symbols = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        list_s = list(s)

        i = 0

        while i < len(list_s) - 1:
            current_val = symbols[list_s[i]]
            next_val = symbols[list_s[i + 1]]

            if current_val < next_val:
                result += (next_val - current_val)
                i += 2

            else:
                result += current_val
                i += 1

        if i < len(list_s):
            result += symbols[list_s[i]]

        return result
