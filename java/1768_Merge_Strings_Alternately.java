// Problem: 1768 - Merge Strings Alternately
// Source: https://leetcode.com/problems/merge-strings-alternately/description/
// Date: 10-19-2024

/*******************************************************************************************************
 *  
 *  UNDERSTANDING
 *  
 *  We are given two strings that we can merge at the same by getting the character of a specific 
 *  index from both strings. If one string is shorter than the other, continue adding the remaining 
 *  characters to the result.
 * 
 *  APPROACH
 * 
 *  1) Initialize an empty ArrayList to store the added characters. The use of ArrayLists or Lists 
 *     allows you to add as many elements as you can unlike a regular array where it has a fixed size.
 *  2) Create a for loop to iterate through each character of both strings according to its index.
 *  3) Calculate the total size of the resulting string to determine how many iterations must be done.
 *  4) Create an if-statement to check if 'i' is a valid index for word1 and word2.
 *  5) Use .charAt method to extract the specific character at index 'i'.
 *  6) Use Character.toString method to convert the character to string before adding it to the result, 
 *     because ArrayLists cannot convert a character to a string. 
 *  7) Use .join method to concatenate all the elements within the resulting list and return the output.
 * 
 *******************************************************************************************************/

import java.util.ArrayList;

class Solution {
    public String mergeAlternately(String word1, String word2) {
        
        ArrayList<String> result = new ArrayList<String>();
        int size = word1.length() + word2.length();

        for (int i = 0; i < size; i++) {
            if (i < word1.length()) {
                char letter = word1.charAt(i);
                result.add(Character.toString(letter));
            }

            if (i <  word2.length()) {
                char letter = word2.charAt(i);
                result.add(Character.toString(letter));
            }
        }

        return String.join("", result);
    }
}