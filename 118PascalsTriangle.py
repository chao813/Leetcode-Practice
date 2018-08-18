"""Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]"""

def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res, row = [], [1]
        for i in range(numRows):
            res.append(row)
            row = [1] + [row[i]+row[i-1] for i in range(1, len(row))] + [1]
        return res 