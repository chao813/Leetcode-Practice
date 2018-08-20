"""Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]"""

def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res, row = [], [1]
        for i in range(rowIndex + 1):
            res.append(row)
            row = [1] + [row[i]+row[i-1] for i in range(1, len(row))] + [1]
        return res[rowIndex]