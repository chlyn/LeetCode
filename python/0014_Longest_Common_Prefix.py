# Problem: 0014 - Longest Common Prefix
# Source: https://leetcode.com/problems/longest-common-prefix/
# Date: 11-16-2024

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        result = ""

        strs.sort(key = len)
        short_word = strs[0]
        word_len = len(strs[0])

        for word in strs:

            while word_len >= 0:
                if short_word[:word_len] == word[:word_len]:
                    result = short_word[:word_len]
                    break

                word_len -= 1

        return result