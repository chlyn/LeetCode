# Problem: 1768 - Merge Strings Alternately
# Source: https://leetcode.com/problems/merge-strings-alternately/description/
# Date: 10-19-2024

########################################################################################################## 
#  
#  UNDERSTANDING
#    
#  We are given two strings that we can merge at the same by getting the character of a specific 
#  index from both strings. If one string is shorter than the other, continue adding the remaining 
#  characters to the result.
#   
#  APPROACH
#   
#  1) Initialize an empty array to store the added characters. 
#  2) Create a for loop to iterate through each character of both strings according to its index.
#  3) Calculate the total size of the resulting string to determine how many iterations must be done.
#  4) Create an if-statement to check if 'i' is a valid index for word1 and word2.
#  5) Use .append method to add the letter in the resulting list.
#  7) Use .join method to concatenate all the elements within the resulting list and return the output.
#
#########################################################################################################

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        result = []

        for i in range (len(word1) + len(word2)):
            if i < len(word1):  
                result.append(word1[i])

            if i < len(word2):
                result.append(word2[i])

        return ''.join(result)