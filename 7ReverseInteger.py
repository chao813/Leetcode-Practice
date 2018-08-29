"""Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows."""

def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x < 0:
            result = (0 - int(str(0-x)[::-1]))
            if result <= 2147483647 and result >= -2147483648:
                return result
            else:
                return 0
        else:
            result = int(str(x)[::-1])
            if result <= 2147483647 and result >= -2147483648:
                return result
            else:
                return 0
        