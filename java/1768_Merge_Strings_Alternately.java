// [1768] Merge Strings Alternately

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