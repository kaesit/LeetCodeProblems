class Solution:
     def isValid(self, s: str):
          stack = []
          mapping = {
               '(': ')',
               '{': '}',
               '[': ']'
          }
          """if s == "()" or s == "{}" or s == "[]":
               return True"""
          for element in s:
               if element in mapping:
                    stack.append(element)
               elif len(stack) == 0 or element != mapping[stack.pop()]:
                    return False
          return len(stack) == 0