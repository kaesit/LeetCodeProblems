from typing import List
class Solution:
     def generate(self, numRows: int) -> List[List[int]]:
          res = []
          triangle = []
          prev_row = []
          for i in range(0, numRows + 1):
               """C = 1
               for j in range(1, i + 1):
                    C = int(C * (i - j) / j);
                    res.append([C])"""
               res = [j > 0 and j < i - 1 and i > 2 and prev_row[j-1] + prev_row[j] or 1 for j in range(0, i)]
               prev_row = res
               triangle += [res]
          return triangle[1:]
     
     """def binom(self, n, k):
          res = 1
          if (k > n - k) :
               k = n - k
          for i in range(0 , k) :
               res = (res * (n - i))
               res = (res // (i + 1))
          
          return res"""
   
print(Solution().generate(3))

import re
string = "A man, a plan, a canal: Panama"
dict_of_symbols = {}
cleaned_string = re.sub(r'[^a-zA-Z]', '', string)
print(cleaned_string.lower())
print(cleaned_string[0::])

class Solution2:
     def isPalindrome(self, s: str) -> bool:
          cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s)
          ne = cleaned_string.lower()
          print(ne)
          if ne[0::] == ne[::-1]:
               return True
          else:
               return False
          
print(Solution2().isPalindrome("0P"))

def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  
  # turn the set into a list (as requested)
  return list( seen_twice )

a = [1,2,3,2,1,5,6,5,5,5]
print(list_duplicates(a)) # yields [1, 2, 5]

a = [[1], [2], [3], [1], [3], [5], [3]]

no_dupes = [x for n, x in enumerate(a) if x not in a[:n]]
print (no_dupes) # [[1], [2], [3], [5]]

dupes = [x for n, x in enumerate(a) if x in a[:n]]
print (dupes) # [[1], [3]]

print(no_dupes.index([1]))
print(no_dupes)

a:str
print(a) 

n = input()
res = []


class Solution3:
     def generateParenthesis(self, n: int) -> List[str]:
          
          def replacing(n:int):
               pass
          res = []
          a = "".join("()")
          if 1 <= n <= 8:
               if n == 1:
                    res.append("()")
               else:
                    for i in range(n+2):
                         a += "".join(f"{('()' * i)}")
                         #res.insert(i, "()")
               res.append(a)

          return res
     
print(Solution3().generateParenthesis(3))
     