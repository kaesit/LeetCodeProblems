class Solution:
     def isValid(self, s: str) -> bool:
          un_recorded = ["(]", "[)", "(}", "{)", "{]", "[}"]
          if s == "()" or s == "{}" or s == "[]":
               return True
          if "(]" or "[)" or "(}" or "{)" or "{]" or "[}" not in s:
               return True
          for element in un_recorded:
               if element not in s:
                    return True
               else:
                    return False

print(Solution().isValid("(])"))

from typing import List
class Solution2:
     def plusOne(self, digits: List[int]) -> List[int]:
          adding = ""
          res = 0
          string_number = ""
          num_list_string = map(str, digits)
          string_number = adding.join(num_list_string)
          string_number = int(string_number)
          string_number += 1
          res = [int(x) for x in str(string_number)]
          print(res)
        
Solution2().plusOne([1, 2, 3])

"""
class Solution3:
     def lengthOfLastWord(self, s: str) -> int:
          a = s.split()
          n = len(a[-1])
          return n

print(Solution3().lengthOfLastWord("Hello World"))

"""

a = 19
c = a
b = str(a)
"""b = a.split()
print(b)"""
i = 0
"""while True:
     res = 0
     for j in str(c):
          i += int(j) ** 2
     if res == 1:
          print(True)
     else:
          print(False)
     i += 1"""

print("")

def recursive(n:int):
     temp = n
     c = False
     res = 0
     for i in str(temp):
          res += int(i) ** 2
          if res == 1:
               c = True
               break
          elif res != 1:
               c = False
          else:
               recursive(n)
               c = False
     return c


print(recursive(56))
     

          

"""print(res)"""


"""print(res)"""
