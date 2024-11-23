class Solution(object):
     def isPalindrome(self, x):
          check = False
          string_number = str(x)
          new_number = string_number[::-1]
          if new_number == string_number:
               check = True
          else:
               check = False
          return check
Solution().isPalindrome(15)
        