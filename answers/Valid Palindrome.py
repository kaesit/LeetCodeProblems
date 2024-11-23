import re
class Solution:
     def isPalindrome(self, s: str) -> bool:
          cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s)
          ne = cleaned_string.lower()
          if ne[0::] == ne[::-1]:
               return True
          else:
               return False