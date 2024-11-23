class Solution:
     def uniquePaths(self, m: int, n: int) -> int:
          mem = {}
     
          for i in range(1, n + 1):
               mem[(i, 1)] = 1
          for j in range(1, m + 1):
               mem[(1, j)] = 1
          
          for i in range(2, n + 1):
               for j in range(2, m + 1):
                    mem[(i, j)] = mem[(i - 1, j)] + mem[(i, j - 1)]
          return mem[(n, m)]