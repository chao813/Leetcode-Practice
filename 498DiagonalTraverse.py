"""Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:
zig zag the numbers"""


def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        lines = collections.defaultdict(list)
        for i in range(len(matrix)):  #row
            for j in range(len(matrix[0])): #column
                lines[i+j].append(matrix[i][j])    #since all diagonals = row + column
                
        for k in sorted(dd.keys()):
            if k%2==1: dd[k].reverse()
            result += dd[k]
        return result


