class Solution:
     def myPow(self, x: float, n: int) -> float:
          res:float = 0
          if -100 < x < 100 or -(2**31) <= n <= (2**31)-1 or x!=0:
               if n == 0:
                    res = 1
               if n < 1 and x > 1:
                    n = abs(n)
                    res = (1 / (x ** n))
               
               else:
                    res = x**n
          return res
     
print(Solution().myPow(2, -2))
print(Solution().myPow(2, 2))
print(Solution().myPow(2, 1))
"""n = abs(-2)
res = 1 / (2 ** n)
print(res)"""
