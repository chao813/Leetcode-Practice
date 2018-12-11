"""Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99"""


def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=[]
        tmp=9
        for i in range(9,0,-1):
            ans.append(tmp)
            tmp*=i
            
        print(ans)
        
        return sum(ans[:n])+1