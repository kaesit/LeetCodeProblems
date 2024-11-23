from typing import List
class Solution:
     def rotate(self, matrix: List[List[int]]) -> None:
          pass
     

matrix:List[List[int]] = [[1,2,3],[4,5,6],[7,8,9]]
#print(a[1][::-1])
n = len(matrix)
print(matrix)
"""matrix[0][1] = matrix[1][-1]
res = []
res = matrix[::-1]"""
"""for i in range(0, len(matrix)):
     #res.append([a[-1][i], a[i - 1][i], a[0][i]])
     #res.append(matrix[i][::-1])
     #res[-1][i] = res[i][-1]
     for j in range(i):
          res[-i][j] = res[i][-j]"""
     
top = 0
bottom = n - 1

print("Matrix: ", matrix)
#print("Res: ", res)

"""while top < bottom:
     for col in range(n):
          temp = matrix[top][col]
          matrix[top][col] = matrix[bottom][col]
          matrix[bottom][col] = temp
     top += 1
     bottom -= 1

for row in range(n):
     for col in range(row+1, n):
          temp = matrix[row][col]
          matrix[row][col] = matrix[col][row]
          matrix[col][row] = temp
"""



for row in range(n):
     for col in range(row + 1, n):
          temp = matrix[row][col]
          matrix[row][col] = matrix[col][row]
          matrix[col][row] = temp
new_array = []

for i in range(n - 1):
     temp = matrix[top][col]
     matrix[top][col] = matrix[bottom][col]
     matrix[bottom][col] = temp
     new_array = matrix

print("New Matrix: ", new_array)

class Solution2:
     def rotate(self, matrix: List[List[int]]) -> None:
          def transpose(matrix):
               for i in range(len(matrix)):
                    for j in range(i, len(matrix[0])):
                         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

          def reverse_rows(matrix):
               for i in range(0, len(matrix)):
                    matrix[i] = matrix[i][::-1]

          transpose(matrix)
          reverse_rows(matrix)
          return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution2().rotate(matrix))