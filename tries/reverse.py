from typing import List
"""res = ["h","e","l","l","o"]
a = "".join(str(x) for x in res)
print(a)
print(a[::-1])
print(list(a[::-1]))
"""

class Solution:
     def reverseString(self, s: List[str]) -> None:
          s[:] = s[::-1]
          return s
     
print(Solution().reverseString(["h","e","l","l","o"]))
        
