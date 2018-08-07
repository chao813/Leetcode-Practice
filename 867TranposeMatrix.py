"""Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 """


def transpose(self, A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    temp = []
    final = []
    i = 0
    
    while i != len(A[0]):
        for lists in A:
            temp.append(lists[i])
        i = i + 1
        final.append(temp)
        temp =[]
        
    return final
        