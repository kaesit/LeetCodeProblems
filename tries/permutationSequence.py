"""
def factorial(n):
     if n == 0:
          return 1
     else:
          return n * factorial(n - 1)

def _line(n, k):
     lin = []
     for i in range(n - 1, 0, -1):
        quotient, remainder = k // factorial(i), k % factorial(i)
        lin.append(quotient)
        k = remainder
     return lin
     

class Solution():
     def getPermutation(self, n: int, k: int, i = 0) -> str:
          line = _line(n,k)
          res = ''
          array = [str(i) for i in range(0, n)]
          while line :
               index = line.pop(0)
               res += array[index]
               del array[index]
          res += array[0]
          return res 
          
          
          

print(Solution().getPermutation(3, 3))"""

#print(factorial(5))



"""def recursive(new_p, aft):
            if not aft:
                # No more elements to permute, add the current path to the result
                new_list.append(new_p)
                return
            for i in range(len(aft)):
                # Recur with the current element added to the path
                # and the remaining elements excluding the current one
                recursive(new_p + [aft[i]], aft[:i] + aft[i + 1:])
          recursive([], the_list)
          ak = new_list[k]
          return ak
"""

def factorial(n):
     if n == 0 : 
          return 1
     else:
          return n * factorial(n-1)

def _line(n, k):
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

x = {'foo', 'bar', 'baz', 'foo', 'qux'}
x = list(x)
print(x)
