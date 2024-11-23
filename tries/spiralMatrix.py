from typing import List

res  = []
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rows, cols = len(matrix), len(matrix[0])
x, y, dx, dy = 0, 0, 1, 0
for _ in range(rows * cols):
     res.append(matrix[y][x])
     matrix[y][x] = "."
     if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y + dy][x + dx] == ".":
          dx, dy = -dy, dx
            
     x += dx
     y += dy
print(res)

class Solution:
     def solve(self, matrix: List[List[int]]) -> List[int]:
          res = []
          rows, cols = len(matrix), len(matrix[0])
          x, y, dx, dy = 0, 0, 1, 0
          for _ in range(rows * cols):
               res.append(matrix[y][x])
               matrix[y][x] = "."
               if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y + dy][x + dx] == ".":
                    dx, dy = -dy, dx
                         
               x += dx
               y += dy
          return res
     
     
matrix = [[1,2,3],[4,5,6],[7,8,9]]
if __name__ == '__main__':
     print(Solution().solve(matrix))
          