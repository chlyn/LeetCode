# Problem: 0412 - Fizz Buzz
# Source: https://leetcode.com/problems/fizz-buzz/
# Date: 11-18-2024

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        results = []

        for i in range (1, n + 1):
            if (i % 3 == 0) and (i % 5 == 0):
                results.append("FizzBuzz")
            elif (i % 3 == 0):
                results.append("Fizz")
            elif (i % 5 == 0):
                results.append("Buzz")
            else:
                results.append(str(i))

        return results