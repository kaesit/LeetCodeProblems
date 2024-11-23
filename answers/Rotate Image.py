class Solution:
     def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
          n = len(matrix)
          for row in range(len(matrix)):
               for column in range(row, len(matrix[0])):
                    matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]
          for i in range(0, n):
               matrix[i] = matrix[i][::-1]
          return matrix