class Solution:
     def generate(self, numRows: int) -> List[List[int]]:
          res = []
          triangle = []
          prev_row = []
          for i in range(0, numRows + 1):
               res = [j > 0 and j < i - 1 and i > 2 and prev_row[j-1] + prev_row[j] or 1 for j in range(0, i)]
               prev_row = res
               triangle += [res]
          return triangle[1:]