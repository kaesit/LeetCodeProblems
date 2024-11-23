def factorial(n):
     if n == 0 : 
          return 1
     else:
          return n * factorial(n-1)

def _line(n,k):
     lin = []
     k = k - 1
     for i in range(n-1,0,-1):
          liner, remainder = k // factorial(i), k % factorial(i)
          lin.append(liner)
          k = remainder
     return lin

class Solution:
     def getPermutation(self, n: int, k: int) -> str:
          control = factorial(n)
          if k > control:
               return None
          liner = _line(n,k)
          res = ''
          array = [str(i) for i in range(1, n + 1)]
          while liner :
               index = liner.pop(0)
               res +=array[index]
               del array[index]
          res +=array[0]
          return res 

print(Solution().getPermutation(3, 3))