
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        
        for i in range(n):
            for j in range(n):
                if i==j:
                    break
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        self.reverseEachRow(matrix)
        return matrix
      
    def reverseEachRow(self,mat):
        for i in range(len(mat)):
            mat[i]=mat[i][::-1]
            